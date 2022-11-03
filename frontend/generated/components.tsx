import gql from 'graphql-tag';
import * as Urql from 'urql';
export type Maybe<T> = T | null;
export type InputMaybe<T> = Maybe<T>;
export type Exact<T extends { [key: string]: unknown }> = { [K in keyof T]: T[K] };
export type MakeOptional<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]?: Maybe<T[SubKey]> };
export type MakeMaybe<T, K extends keyof T> = Omit<T, K> & { [SubKey in K]: Maybe<T[SubKey]> };
export type Omit<T, K extends keyof T> = Pick<T, Exclude<keyof T, K>>;
/** All built-in and custom scalars, mapped to their actual values */
export type Scalars = {
  ID: string;
  String: string;
  Boolean: boolean;
  Int: number;
  Float: number;
};

export type FruitType = {
  __typename?: 'FruitType';
  eatenBy?: Maybe<PersonType>;
  id: Scalars['String'];
  name: Scalars['String'];
};

/** Create/Update/Delete operations */
export type Mutation = {
  __typename?: 'Mutation';
  addFruit: FruitType;
  addPerson: PersonType;
  removePerson: PersonType;
};


/** Create/Update/Delete operations */
export type MutationAddFruitArgs = {
  name: Scalars['String'];
};


/** Create/Update/Delete operations */
export type MutationAddPersonArgs = {
  name: Scalars['String'];
};


/** Create/Update/Delete operations */
export type MutationRemovePersonArgs = {
  byId: Scalars['String'];
};

export type PersonType = {
  __typename?: 'PersonType';
  id: Scalars['String'];
  name: Scalars['String'];
  surname?: Maybe<Scalars['String']>;
};

/** Read Operations */
export type Query = {
  __typename?: 'Query';
  /** Read all fruits. */
  fruits: Array<FruitType>;
  /** Get a person from ID */
  getPerson: PersonType;
  /** Read all persons. */
  persons: Array<PersonType>;
};


/** Read Operations */
export type QueryGetPersonArgs = {
  id: Scalars['String'];
};

export type Subscription = {
  __typename?: 'Subscription';
  count: Scalars['Int'];
};


export type SubscriptionCountArgs = {
  target?: Scalars['Int'];
};

export type AddPersonMutationVariables = Exact<{
  name: Scalars['String'];
}>;


export type AddPersonMutation = { __typename?: 'Mutation', addPerson: { __typename?: 'PersonType', id: string, name: string, surname?: string | null } };

export type FetchPersonListQueryVariables = Exact<{ [key: string]: never; }>;


export type FetchPersonListQuery = { __typename?: 'Query', persons: Array<{ __typename?: 'PersonType', id: string, name: string, surname?: string | null }> };

export type RemovePersonMutationVariables = Exact<{
  byId: Scalars['String'];
}>;


export type RemovePersonMutation = { __typename?: 'Mutation', removePerson: { __typename?: 'PersonType', id: string, name: string } };


export const AddPersonDocument = gql`
    mutation AddPerson($name: String!) {
  addPerson(name: $name) {
    id
    name
    surname
  }
}
    `;

export function useAddPersonMutation() {
  return Urql.useMutation<AddPersonMutation, AddPersonMutationVariables>(AddPersonDocument);
};
export const FetchPersonListDocument = gql`
    query FetchPersonList {
  persons {
    id
    name
    surname
  }
}
    `;

export function useFetchPersonListQuery(options?: Omit<Urql.UseQueryArgs<FetchPersonListQueryVariables>, 'query'>) {
  return Urql.useQuery<FetchPersonListQuery, FetchPersonListQueryVariables>({ query: FetchPersonListDocument, ...options });
};
export const RemovePersonDocument = gql`
    mutation RemovePerson($byId: String!) {
  removePerson(byId: $byId) {
    id
    name
  }
}
    `;

export function useRemovePersonMutation() {
  return Urql.useMutation<RemovePersonMutation, RemovePersonMutationVariables>(RemovePersonDocument);
};