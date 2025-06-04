import { APIGatewayProxyEventV2, APIGatewayProxyResultV2 } from "aws-lambda";
import { generateQrCode, QRCodeOptions } from "./qrCodeGenerator";

/**
 * AWS Lambda ハンドラ関数
 * @param event API Gateway からのイベント
 * @returns HTTP レスポンス
 */
export const handler = async (event: APIGatewayProxyEventV2): Promise<APIGatewayProxyResultV2> => {
  try {
    // リクエストボディから QR コードのオプションと出力タイプを取得
    const body = event.body ? JSON.parse(event.body) : {};
    const qrCodeOptions: QRCodeOptions = body.qrCodeOptions || {};
    const outputType: "png" | "svg" = body.outputType === "svg" ? "svg" : "png"; // デフォルトは 'png'

    // 必須データが不足している場合はエラー
    if (!qrCodeOptions.data) {
      return {
        statusCode: 400,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: "Missing required parameter: data" }),
      };
    }

    // QR コードを生成
    const qrCodeBuffer = await generateQrCode(qrCodeOptions, outputType);

    // 生成された QR コードのタイプに応じて Content-Type を設定
    const contentType = outputType === "svg" ? "image/svg+xml" : "image/png";

    return {
      statusCode: 200,
      headers: {
        "Content-Type": contentType,
        "Access-Control-Allow-Origin": "*", // CORS を許可
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
      },
      body: qrCodeBuffer.toString("base64"), // バイナリデータを Base64 エンコードして返す
      isBase64Encoded: true, // Base64 エンコードされていることを Lambda に伝える
    };
  } catch (error) {
    console.error("Error generating QR code:", error);
    return {
      statusCode: 500,
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        message: "Failed to generate QR code",
        error: (error as Error).message,
      }),
    };
  }
};
