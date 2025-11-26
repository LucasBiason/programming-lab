import Image from "next/image";
import Link from "next/link";
import styles from '../page.module.css';

async function getData(){
    const response = await fetch("https://pokeapi.co/api/v2/pokemon/");
    return response.json();
}

export default async function Pokemons() {
  const { results } = await getData();

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <h1>Pokemons</h1>
          <ul className={styles.verticalMenu}>
              {
                results 
                ? results.map((pokemon, index) => (
                    <li key={index} className={styles.menuItem} >
                      <Link href={`/pokemons/${pokemon.name}`}>{pokemon.name}
                      </Link>
                    </li>
                )) 
                : Nenhum
              }
            </ul>
      </main>
    </div>
  );
}
