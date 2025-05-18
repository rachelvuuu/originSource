export default async function handler(req, res) {
  res.writeHead(200, { "Content-Type": "text/plain" });
  let i = 0;
  const interval = setInterval(() => {
    if (i >= 5) {
      clearInterval(interval);
      res.end("✅ Done slow sending.");
    } else {
      res.write("Chunk " + i + "\n");
      i++;
    }
  }, 1000);
}