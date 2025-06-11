import { APIGatewayProxyStructuredResultV2, LambdaFunctionURLEvent } from "aws-lambda";
import { beforeEach, describe, expect, it, vi } from "vitest";
import { handler } from "./index";
import * as qrCodeGenerator from "./qrCodeGenerator";

// qrCodeGenerator モジュールをモック
vi.mock("./qrCodeGenerator", () => ({
  generateQRCode: vi.fn(),
}));

const mockGenerateQRCode = vi.mocked(qrCodeGenerator.generateQRCode);

describe("Lambda handler", () => {
  beforeEach(() => {
    vi.clearAllMocks();
  });

  it("should generate QR code with PNG format by default", async () => {
    const mockBuffer = Buffer.from("mock-png-data");
    mockGenerateQRCode.mockResolvedValue(mockBuffer);

    const event: LambdaFunctionURLEvent = {
      version: "2.0",
      routeKey: "$default",
      rawPath: "/qrcode/test",
      rawQueryString: "",
      cookies: [],
      headers: {
        host: "example.com",
      },
      queryStringParameters: {},
      requestContext: {
        accountId: "123456789012",
        apiId: "api-id",
        domainName: "example.com",
        domainPrefix: "api",
        http: {
          method: "POST",
          path: "/qrcode/test",
          protocol: "HTTP/1.1",
          sourceIp: "127.0.0.1",
          userAgent: "Custom User Agent String",
        },
        requestId: "id",
        routeKey: "$default",
        stage: "$default",
        time: "12/Mar/2020:19:03:58 +0000",
        timeEpoch: 1583348638390,
      },
      body: JSON.stringify({
        qrCodeOptions: {
          width: 256,
          height: 256,
        },
        outputType: "png",
      }),
      pathParameters: {},
      isBase64Encoded: false,
      stageVariables: {},
    };

    const result = (await handler(event)) as APIGatewayProxyStructuredResultV2;

    expect(result.statusCode).toBe(200);
    expect(result.headers?.["Content-Type"]).toBe("image/png");
    expect(result.body).toBe(mockBuffer.toString("base64"));
    expect(result.isBase64Encoded).toBe(true);
    expect(mockGenerateQRCode).toHaveBeenCalledWith(
      {
        width: 256,
        height: 256,
        data: "https://example.com/test",
      },
      "png",
    );
  });

  it("should generate QR code with SVG format when specified", async () => {
    const mockBuffer = Buffer.from("<svg>mock-svg-data</svg>");
    mockGenerateQRCode.mockResolvedValue(mockBuffer);

    const event: LambdaFunctionURLEvent = {
      version: "2.0",
      routeKey: "$default",
      rawPath: "/qrcode/svg-test",
      rawQueryString: "",
      cookies: [],
      headers: {
        host: "api.example.com",
      },
      queryStringParameters: {},
      requestContext: {
        accountId: "123456789012",
        apiId: "api-id",
        domainName: "example.com",
        domainPrefix: "api",
        http: {
          method: "POST",
          path: "/qrcode/svg-test",
          protocol: "HTTP/1.1",
          sourceIp: "127.0.0.1",
          userAgent: "Custom User Agent String",
        },
        requestId: "id",
        routeKey: "$default",
        stage: "$default",
        time: "12/Mar/2020:19:03:58 +0000",
        timeEpoch: 1583348638390,
      },
      body: JSON.stringify({
        qrCodeOptions: {
          dotsOptions: {
            color: "#FF0000",
          },
        },
        outputType: "svg",
      }),
      pathParameters: {},
      isBase64Encoded: false,
      stageVariables: {},
    };

    const result = (await handler(event)) as APIGatewayProxyStructuredResultV2;

    expect(result.statusCode).toBe(200);
    expect(result.headers?.["Content-Type"]).toBe("image/svg+xml");
    expect(result.body).toBe(mockBuffer.toString("base64"));
    expect(result.isBase64Encoded).toBe(true);
    expect(mockGenerateQRCode).toHaveBeenCalledWith(
      {
        dotsOptions: {
          color: "#FF0000",
        },
        data: "https://api.example.com/svg-test",
      },
      "svg",
    );
  });

  it("should handle empty body gracefully", async () => {
    const mockBuffer = Buffer.from("mock-default-data");
    mockGenerateQRCode.mockResolvedValue(mockBuffer);

    const event: LambdaFunctionURLEvent = {
      version: "2.0",
      routeKey: "$default",
      rawPath: "/qrcode/empty-body",
      rawQueryString: "",
      cookies: [],
      headers: {
        host: "localhost:3000",
      },
      queryStringParameters: {},
      requestContext: {
        accountId: "123456789012",
        apiId: "api-id",
        domainName: "example.com",
        domainPrefix: "api",
        http: {
          method: "POST",
          path: "/qrcode/empty-body",
          protocol: "HTTP/1.1",
          sourceIp: "127.0.0.1",
          userAgent: "Custom User Agent String",
        },
        requestId: "id",
        routeKey: "$default",
        stage: "$default",
        time: "12/Mar/2020:19:03:58 +0000",
        timeEpoch: 1583348638390,
      },
      body: undefined,
      pathParameters: {},
      isBase64Encoded: false,
      stageVariables: {},
    };

    const result = (await handler(event)) as APIGatewayProxyStructuredResultV2;

    expect(result.statusCode).toBe(200);
    expect(result.headers?.["Content-Type"]).toBe("image/png");
    expect(mockGenerateQRCode).toHaveBeenCalledWith(
      {
        data: "https://localhost:3000/empty-body",
      },
      "png",
    );
  });

  it("should return 400 error when path doesn't contain /qrcode", async () => {
    const event: LambdaFunctionURLEvent = {
      version: "2.0",
      routeKey: "$default",
      rawPath: "/invalid/path",
      rawQueryString: "",
      cookies: [],
      headers: {
        host: "example.com",
      },
      queryStringParameters: {},
      requestContext: {
        accountId: "123456789012",
        apiId: "api-id",
        domainName: "example.com",
        domainPrefix: "api",
        http: {
          method: "POST",
          path: "/invalid/path",
          protocol: "HTTP/1.1",
          sourceIp: "127.0.0.1",
          userAgent: "Custom User Agent String",
        },
        requestId: "id",
        routeKey: "$default",
        stage: "$default",
        time: "12/Mar/2020:19:03:58 +0000",
        timeEpoch: 1583348638390,
      },
      body: undefined,
      pathParameters: {},
      isBase64Encoded: false,
      stageVariables: {},
    };

    const result = (await handler(event)) as APIGatewayProxyStructuredResultV2;

    expect(result.statusCode).toBe(400);
    expect(result.headers?.["Content-Type"]).toBe("application/json");
    expect(JSON.parse(result.body as string)).toEqual({
      message: "Invalid path: must contain /qrcode",
    });
    expect(mockGenerateQRCode).not.toHaveBeenCalled();
  });

  it("should handle missing host header gracefully", async () => {
    const mockBuffer = Buffer.from("mock-data");
    mockGenerateQRCode.mockResolvedValue(mockBuffer);

    const event: LambdaFunctionURLEvent = {
      version: "2.0",
      routeKey: "$default",
      rawPath: "/qrcode/no-host",
      rawQueryString: "",
      cookies: [],
      headers: {},
      queryStringParameters: {},
      requestContext: {
        accountId: "123456789012",
        apiId: "api-id",
        domainName: "example.com",
        domainPrefix: "api",
        http: {
          method: "POST",
          path: "/qrcode/no-host",
          protocol: "HTTP/1.1",
          sourceIp: "127.0.0.1",
          userAgent: "Custom User Agent String",
        },
        requestId: "id",
        routeKey: "$default",
        stage: "$default",
        time: "12/Mar/2020:19:03:58 +0000",
        timeEpoch: 1583348638390,
      },
      body: undefined,
      pathParameters: {},
      isBase64Encoded: false,
      stageVariables: {},
    };

    const result = (await handler(event)) as APIGatewayProxyStructuredResultV2;

    expect(result.statusCode).toBe(200);
    expect(mockGenerateQRCode).toHaveBeenCalledWith(
      {
        data: "https:///no-host",
      },
      "png",
    );
  });

  it("should return 500 error when QR code generation fails", async () => {
    const mockError = new Error("QR code generation failed");
    mockGenerateQRCode.mockRejectedValue(mockError);

    const event: LambdaFunctionURLEvent = {
      version: "2.0",
      routeKey: "$default",
      rawPath: "/qrcode/error-test",
      rawQueryString: "",
      cookies: [],
      headers: {
        host: "example.com",
      },
      queryStringParameters: {},
      requestContext: {
        accountId: "123456789012",
        apiId: "api-id",
        domainName: "example.com",
        domainPrefix: "api",
        http: {
          method: "POST",
          path: "/qrcode/error-test",
          protocol: "HTTP/1.1",
          sourceIp: "127.0.0.1",
          userAgent: "Custom User Agent String",
        },
        requestId: "id",
        routeKey: "$default",
        stage: "$default",
        time: "12/Mar/2020:19:03:58 +0000",
        timeEpoch: 1583348638390,
      },
      body: undefined,
      pathParameters: {},
      isBase64Encoded: false,
      stageVariables: {},
    };

    const consoleErrorSpy = vi.spyOn(console, "error").mockImplementation(() => {});

    const result = (await handler(event)) as APIGatewayProxyStructuredResultV2;

    expect(result.statusCode).toBe(500);
    expect(result.headers?.["Content-Type"]).toBe("application/json");
    expect(JSON.parse(result.body as string)).toEqual({
      message: "Failed to generate QR code",
      error: "QR code generation failed",
    });
    expect(consoleErrorSpy).toHaveBeenCalledWith("Error generating QR code:", mockError);

    consoleErrorSpy.mockRestore();
  });

  it("should handle invalid JSON in body gracefully", async () => {
    const event: LambdaFunctionURLEvent = {
      version: "2.0",
      routeKey: "$default",
      rawPath: "/qrcode/invalid-json",
      rawQueryString: "",
      cookies: [],
      headers: {
        host: "example.com",
      },
      queryStringParameters: {},
      requestContext: {
        accountId: "123456789012",
        apiId: "api-id",
        domainName: "example.com",
        domainPrefix: "api",
        http: {
          method: "POST",
          path: "/qrcode/invalid-json",
          protocol: "HTTP/1.1",
          sourceIp: "127.0.0.1",
          userAgent: "Custom User Agent String",
        },
        requestId: "id",
        routeKey: "$default",
        stage: "$default",
        time: "12/Mar/2020:19:03:58 +0000",
        timeEpoch: 1583348638390,
      },
      body: "invalid json {",
      pathParameters: {},
      isBase64Encoded: false,
      stageVariables: {},
    };

    const consoleErrorSpy = vi.spyOn(console, "error").mockImplementation(() => {});

    const result = (await handler(event)) as APIGatewayProxyStructuredResultV2;

    expect(result.statusCode).toBe(500);
    expect(result.headers?.["Content-Type"]).toBe("application/json");
    expect(JSON.parse(result.body as string)).toEqual({
      message: "Failed to generate QR code",
      error: expect.stringContaining("Unexpected token"),
    });

    consoleErrorSpy.mockRestore();
  });

  it("should construct correct URL when rawPath has complex path after /qrcode", async () => {
    const mockBuffer = Buffer.from("mock-data");
    mockGenerateQRCode.mockResolvedValue(mockBuffer);

    const event: LambdaFunctionURLEvent = {
      version: "2.0",
      routeKey: "$default",
      rawPath: "/api/v1/qrcode/user/123/profile",
      rawQueryString: "",
      cookies: [],
      headers: {
        host: "api.example.com",
      },
      queryStringParameters: {},
      requestContext: {
        accountId: "123456789012",
        apiId: "api-id",
        domainName: "example.com",
        domainPrefix: "api",
        http: {
          method: "POST",
          path: "/api/v1/qrcode/user/123/profile",
          protocol: "HTTP/1.1",
          sourceIp: "127.0.0.1",
          userAgent: "Custom User Agent String",
        },
        requestId: "id",
        routeKey: "$default",
        stage: "$default",
        time: "12/Mar/2020:19:03:58 +0000",
        timeEpoch: 1583348638390,
      },
      body: undefined,
      pathParameters: {},
      isBase64Encoded: false,
      stageVariables: {},
    };

    const result = (await handler(event)) as APIGatewayProxyStructuredResultV2;

    expect(result.statusCode).toBe(200);
    expect(mockGenerateQRCode).toHaveBeenCalledWith(
      {
        data: "https://api.example.com/user/123/profile",
      },
      "png",
    );
  });
});
