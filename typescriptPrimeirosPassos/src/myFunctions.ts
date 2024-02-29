import { User } from './types/User';

export const getUserNames = (userList: User[]): string[] => userList.map((user: User) => user.name);  


//faz uma pesquisa que filtra os usuarios pelo numero de repositorios 
export const getUsersByRepoQuantity = (users: User[], repos: number): string[] => users
  .filter((user) => user.repositories >= repos).map((user) => user.name);

//retorna um valor bolleano dizendo se a pessoa pesquisada é a mais ativa no GitHub
export const IsMostActiveUser = (name: string, users: User[]): boolean => {
  const mostActiveUser = users.reduce(
    (prev, curr) => 
      (prev.repositories > curr.repositories ? prev : curr),
  );
  return mostActiveUser.name === name;
};