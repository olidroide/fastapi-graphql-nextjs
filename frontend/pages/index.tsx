import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'
import {useAddPersonMutation, useFetchPersonListQuery, useRemovePersonMutation} from "../generated/components";

export default function Home() {
    const [res, executeMutation] = useAddPersonMutation();
    const [removedPersonResult, executeRemovePerson] = useRemovePersonMutation();

    const [result] = useFetchPersonListQuery();
    const {data, fetching, error} = result;

    if (fetching) return <div>Loading...</div>
    if (error) return <div>{error.message}</div>
    if (!data) return <div>No Data!</div>

    return (
        <div className={styles.container}>
            <Head>
                <title>Create Next App</title>
                <meta name="description" content="Generated by create next app"/>
                <link rel="icon" href="/favicon.ico"/>
            </Head>

            <main className={styles.main}>
                RESULTS:
                {data.persons.map((value, index) =>
                    <li key={value.id}>{value.name}
                        <button onClick={() => executeRemovePerson({byId: value.id})}>Remove</button>
                    </li>)}

                <button onClick={() => executeMutation({name: 'creado'})}>
                    Create Person
                </button>
            </main>

            <footer className={styles.footer}>
                <a
                    href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    Powered by{' '}
                    <span className={styles.logo}>
            <Image src="/vercel.svg" alt="Vercel Logo" width={72} height={16}/>
          </span>
                </a>
            </footer>
        </div>
    )
}
