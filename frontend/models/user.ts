export interface IUser {
    id: number;
    username: string;
    roles?: IRole[];
}

export interface IRole {
    id: number;
    name: string;
    permissions?: IPermission[];
}

export interface IPermission {
    id: number;
    name: string;
}

export interface IAuthCredentials {
    username: string;
    password: string;
}

export interface IAuthToken {
    token: string;
    type: string;
}