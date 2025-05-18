export default async function handler(req, res) {
  res.status(200).send("✅ Server received full header. No delay here.");
}