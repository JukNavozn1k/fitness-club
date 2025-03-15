
import type React from "react"

import { useState } from "react"
import { Dumbbell, Eye, EyeOff, User } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"

export default function LoginForm() {
  const [showPassword, setShowPassword] = useState(false)
  const [username, setUsername] = useState("")
  const [password, setPassword] = useState("")

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    // Handle login logic here
    console.log("Login attempt with:", { username, password })
  }

  return (
    <div className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-br from-blue-50 to-blue-100 p-4">
      <div className="w-full max-w-md">
    <Card className="w-full shadow-lg">
      <CardHeader className="space-y-1">
        <div className="flex items-center justify-center mb-2">
          <Dumbbell className="h-10 w-10 text-blue-600" />
        </div>
        <CardTitle className="text-2xl font-bold text-center">Фитнес Клуб</CardTitle>
        <CardDescription className="text-center">Войдите в свой аккаунт для доступа</CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit}>
          <div className="space-y-4">
            <div className="space-y-2">
              <Label htmlFor="username">Имя пользователя</Label>
              <div className="relative">
                <User className="absolute left-3 top-3 h-4 w-4 text-muted-foreground" />
                <Input
                  id="username"
                  placeholder="Введите имя пользователя"
                  className="pl-10"
                  value={username}
                  onChange={(e) => setUsername(e.target.value)}
                  required
                />
              </div>
            </div>
            <div className="space-y-2">
              <Label htmlFor="password">Пароль</Label>
              <div className="relative">
                <Input
                  id="password"
                  type={showPassword ? "text" : "password"}
                  placeholder="Введите пароль"
                  className="pr-10"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                />
                <Button
                  type="button"
                  variant="ghost"
                  size="icon"
                  className="absolute right-0 top-0 h-full px-3 py-2 text-muted-foreground"
                  onClick={() => setShowPassword(!showPassword)}
                >
                  {showPassword ? <EyeOff className="h-4 w-4" /> : <Eye className="h-4 w-4" />}
                  <span className="sr-only">{showPassword ? "Скрыть пароль" : "Показать пароль"}</span>
                </Button>
              </div>
            </div>
            <Button type="submit" className="w-full bg-blue-600 hover:bg-blue-700">
              Войти
            </Button>
          </div>
        </form>
      </CardContent>
      <CardFooter className="flex flex-col space-y-2">
        <div className="text-sm text-center text-muted-foreground">
          <a href="#" className="underline underline-offset-4 hover:text-primary">
            Забыли пароль?
          </a>
        </div>
      </CardFooter>
    </Card>
    </div>
    </div>
  )
}

