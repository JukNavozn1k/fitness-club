import {Link} from "react-router-dom"
import { Dumbbell } from "lucide-react"
import { Button } from "@/components/ui/button"

export default function NotFound() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-background px-4 text-center">
      <div className="space-y-6 max-w-md">
        <div className="flex justify-center">
          <div className="bg-primary/10 p-3 rounded-full">
            <Dumbbell className="h-12 w-12 text-primary" />
          </div>
        </div>
        <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl">404 - Страница не найдена</h1>
        <p className="text-muted-foreground text-lg">
          Упс! Похоже, вы зашли в зону, где даже наши тренеры не смогли найти то, что вы ищете.
        </p>
        <div className="flex flex-col sm:flex-row gap-3 justify-center">
          <Button asChild size="lg">
            <Link to="/">Вернуться на главную</Link>
          </Button>
          <Button variant="outline" asChild size="lg">
            <Link to="/contact">Связаться с нами</Link>
          </Button>
        </div>
      </div>
    </div>
  )
}

