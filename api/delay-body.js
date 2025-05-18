export const config = { api: { bodyParser: false } };

export default async function handler(req, res) {
  const delay = parseInt(req.headers["x-delay"] || "10", 10);
  let body = Buffer.from([]);
  for await (const chunk of req) {
    await new Promise(resolve => setTimeout(resolve, delay * 1000));
    body = Buffer.concat([body, chunk]);
  }
  res.status(200).send(`Client Body Delay completed. Data: ${body.toString()}`);
}