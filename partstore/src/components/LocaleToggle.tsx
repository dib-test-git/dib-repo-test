import type { Locale } from "../locales";

type Props = {
  locale: Locale;
  onChange: (next: Locale) => void;
};

export function LocaleToggle({ locale, onChange }: Props) {
  const next: Locale = locale === "ar" ? "en" : "ar";
  return (
    <button onClick={() => onChange(next)} aria-label="Toggle language">
      {locale === "ar" ? "English" : "العربية"}
    </button>
  );
}
