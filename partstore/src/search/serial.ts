/**
 * Serial-number parsing and validation for Cat machines.
 *
 * Cat serials are typically an 8-character prefix plus a numeric serial.
 * We validate the shape here and leave compatibility lookups to the
 * compatibility service.
 */

const SERIAL_PATTERN = /^[A-Z0-9]{3,8}[0-9]{3,6}$/i;

export type ParsedSerial = {
  prefix: string;
  serial: string;
  raw: string;
};

export function parseSerial(input: string): ParsedSerial | null {
  const cleaned = input.trim().toUpperCase().replace(/\s+/g, "");
  if (!SERIAL_PATTERN.test(cleaned)) {
    return null;
  }
  const match = cleaned.match(/^([A-Z0-9]+?)([0-9]{3,6})$/);
  if (!match) return null;
  return { prefix: match[1], serial: match[2], raw: cleaned };
}
