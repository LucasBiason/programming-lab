"use client" 
import Image from "next/image";
import Link from "next/link";
import styles from '../../page.module.css';
import { useParams } from "next/navigation";
import { useEffect, useState } from "react";


async function getData(pokemon_id){
  const response = await fetch("https://pokeapi.co/api/v2/pokemon/"+pokemon_id);
  return response.json();
}

export default function Pokemons() {
  const params = useParams();
  const [pokemon, setPokemon] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchPokemon = async () => {
      try {
        const data = await getData(params.id);
        setPokemon(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setLoading(false);
      }
    };

    fetchPokemon();
  }, [params.id]);

  if (loading) {
    return <div>Carregando...</div>;
  }

  if (error) {
    return <div>Erro: {error}</div>;
  }

  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <main className="flex flex-col gap-8 row-start-2 items-center sm:items-start">
        <h1>Detalhes do Pokemon</h1>

        {pokemon && (
          <div>
            <h2>{pokemon.name} #({pokemon.order})</h2>
            <Image
              src={pokemon.sprites.front_default}
              alt={pokemon.name}
              width={200}
              height={200}
            />
            <p>Altura: {pokemon.height}</p>
            <p>Peso: {pokemon.weight}</p>
            <p>Tipo: {pokemon.types.map(typeInfo => typeInfo.type.name).join(', ')}</p>
          </div>
        )}
        
         <Link href="/pokemons">
          <button className="mt-4 px-4 py-2 bg-blue-500 text-white rounded">Voltar</button>
        </Link>

      </main>
    </div>
  );
}
