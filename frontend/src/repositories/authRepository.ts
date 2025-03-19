import { $api } from '@/core/api/axios';
import { IAuthCredentials, IAuthToken, IUser } from '@/models/user';

export interface IAuthRepository {
  login(credentials: IAuthCredentials): Promise<IAuthToken>;
  register(credentials: IAuthCredentials): Promise<IUser>;
  getCurrentUser(): Promise<IUser>;
  verifyToken(token: string): Promise<boolean>;
  logout(): Promise<void>;
}

export class AuthRepository implements IAuthRepository {
  async login(credentials: IAuthCredentials): Promise<IAuthToken> {
    const response = await $api.post<IAuthToken>('/auth/login', credentials);
    return response.data;
  }

  async register(credentials: IAuthCredentials): Promise<IUser> {
    const response = await $api.post<IUser>('/auth/register', credentials);
    return response.data;
  }

  async getCurrentUser(): Promise<IUser> {
    const response = await $api.get<IUser>('/auth/me');
    return response.data;
  }

  async verifyToken(token: string): Promise<boolean> {
    const response = await $api.get<{ valid: boolean }>('/auth/verify-token');
    return response.data.valid;
  }

  async logout(): Promise<void> {
    localStorage.removeItem('token');
  }
}

export const authRepository = new AuthRepository();
