import { IAuthCredentials, IUser } from '@/models/user';
import { AuthRepository, authRepository } from '@/repositories/authRepository';

export class AuthService {
  constructor(private repository: AuthRepository) {}

  async login(credentials: IAuthCredentials): Promise<IUser> {
    const token = await this.repository.login(credentials);
    localStorage.setItem('token', token.token);
    return await this.repository.getCurrentUser();
  }

  async register(credentials: IAuthCredentials): Promise<IUser> {
    const user = await this.repository.register(credentials);
    const token = await this.repository.login(credentials);
    localStorage.setItem('token', token.token);
    return user;
  }

  async logout(): Promise<void> {
    await this.repository.logout();
  }

  async getCurrentUser(): Promise<IUser | null> {
    try {
      return await this.repository.getCurrentUser();
    } catch {
      return null;
    }
  }

  async verifyToken(): Promise<boolean> {
    try {
      const token = localStorage.getItem('token');
      if (!token) return false;
      return await this.repository.verifyToken(token);
    } catch {
      return false;
    }
  }
}

export const authService = new AuthService(authRepository);
