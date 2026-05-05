import fleetCatalog from "../data/fleet-catalog.json";

type Machine = (typeof fleetCatalog.machines)[number];

type Props = { country: string };

export default function CatalogPage({ country }: Props) {
  const machines: Machine[] = fleetCatalog.machines.filter((m) =>
    m.countries.includes(country),
  );

  return (
    <main>
      <h1>Rental fleet — {country}</h1>
      <ul>
        {machines.map((m) => (
          <li key={m.model}>
            <strong>{m.model}</strong> ({m.category}) — from ${m.dayRate_USD}/day
          </li>
        ))}
      </ul>
    </main>
  );
}
