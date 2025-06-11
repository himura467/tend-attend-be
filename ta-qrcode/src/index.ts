import { LambdaFunctionURLEvent, LambdaFunctionURLResult } from "aws-lambda";
import { generateQrCode, QRCodeOptions } from "./qrCodeGenerator";

/**
 * AWS Lambda ハンドラ関数
 * @param event Lambda function URLs からのイベント
 * @returns HTTP レスポンス
 */
export const handler = async (event: LambdaFunctionURLEvent): Promise<LambdaFunctionURLResult> => {
  try {
    // リクエストボディから QR コードのオプションと出力タイプを取得
    const body = event.body ? JSON.parse(event.body) : {};
    const qrCodeOptions: QRCodeOptions = body.qrCodeOptions || {};
    const outputType: "png" | "svg" = body.outputType === "svg" ? "svg" : "png"; // デフォルトは 'png'

    const rawPath = event.rawPath || "";
    const host = event.headers?.host || "";

    // /qrcode 以降のパスを取得
    const qrCodeIndex = rawPath.indexOf("/qrcode");
    if (qrCodeIndex === -1) {
      return {
        statusCode: 400,
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: "Invalid path: must contain /qrcode" }),
      };
    }

    const pathAfterQRCode = rawPath.substring(qrCodeIndex + "/qrcode".length);
    const data = `https://${host}${pathAfterQRCode}`;

    // data を qrCodeOptions に設定
    qrCodeOptions.data = data;

    // QR コードを生成
    const qrCodeBuffer = await generateQrCode(qrCodeOptions, outputType);

    // 生成された QR コードのタイプに応じて Content-Type を設定
    const contentType = outputType === "svg" ? "image/svg+xml" : "image/png";

    return {
      statusCode: 200,
      headers: { "Content-Type": contentType },
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
