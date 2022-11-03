import {createClient} from "urql";

// const url = process.env.GRAPHQL_URL;
//
// export const client = createClient({url});

const url = 'http://127.0.0.1:8000/graphql/';

export const client = createClient({url})