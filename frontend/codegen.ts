import type {CodegenConfig} from '@graphql-codegen/cli';

const config: CodegenConfig = {
    overwrite: true,
    schema: "http://127.0.0.1:8000/graphql/",
    documents: "graphql/**/*.graphql",
    generates: {
        'generated/components.tsx': {
            plugins: ['typescript', 'typescript-operations', 'typescript-urql']
        }
    }
};

export default config;
