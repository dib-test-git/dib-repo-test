import en from "./en.json";
import ar from "./ar.json";

export type Locale = "en" | "ar";

export const messages = { en, ar } as const;

export function direction(locale: Locale): "ltr" | "rtl" {
  return locale === "ar" ? "rtl" : "ltr";
}
