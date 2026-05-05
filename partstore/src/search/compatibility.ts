import type { ParsedSerial } from "./serial";

export type PartRef = {
  partNumber: string;
  description: string;
  category: "filter" | "hose" | "undercarriage" | "other";
};

export interface CompatibilityService {
  /** Returns the subset of `candidates` that fit the given machine. */
  filterByMachine(
    serial: ParsedSerial,
    candidates: PartRef[],
  ): Promise<PartRef[]>;
}
