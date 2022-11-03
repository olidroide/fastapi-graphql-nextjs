front typescript created with 
```commandline
yarn global add create-next-app

cd frontend/
npx create-next-app --example with-typescript-graphql .



```

test with https://www.youtube.com/watch?v=EoM-1Lq0rjU

install pnpm
curl -fsSL https://get.pnpm.io/install.sh | sh -

`pnpm create next-app --ts`

name `frontend`

`cd frontend`

`yarn add urql graphql graphql-tag @graphql-codegen/cli`

`mkdir lib`

`touch lib/graphql.ts`

`mkdir graphql`

`touch .graphqlrc.yml`


`yarn graphql-code-generator init`


```commandline
? What type of application are you building? Application built with React
? Where is your schema?: (path or url) http://127.0.0.1:8000/graphql/
? Where are your operations and fragments?: graphql/**/*.graphql
? Where to write the output: generated/graphql.ts
? Do you want to generate an introspection file? No
? How to name the config file? codegen.ts
? What script in package.json should run the codegen? generate
```
`yarn  add @graphql-codegen/typescript-urql`
`yarn generate`
`yarn generate --watch`
`yarn run dev`
