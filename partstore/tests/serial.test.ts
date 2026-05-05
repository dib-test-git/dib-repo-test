import { parseSerial } from "../src/search/serial";

describe("parseSerial", () => {
  it("parses a standard 8-character prefix serial", () => {
    expect(parseSerial("WGN12345")).toEqual({
      prefix: "WGN",
      serial: "12345",
      raw: "WGN12345",
    });
  });

  it("is case-insensitive and strips whitespace", () => {
    expect(parseSerial("  wgn 12345 ")?.raw).toBe("WGN12345");
  });

  it("rejects obviously invalid input", () => {
    expect(parseSerial("!!")).toBeNull();
    expect(parseSerial("")).toBeNull();
  });
});
