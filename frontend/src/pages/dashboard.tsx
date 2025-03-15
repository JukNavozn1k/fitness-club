import {Link} from "react-router-dom"
import { Dumbbell, Calendar, User, CreditCard, BarChart, Menu } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet"
import { Avatar, AvatarFallback, AvatarImage } from "@/components/ui/avatar"
import { Progress } from "@/components/ui/progress"
import { Badge } from "@/components/ui/badge"

export default function Dashboard() {
  return (
    <div className="min-h-screen bg-background">
      {/* Mobile Navigation */}
      <div className="md:hidden flex items-center justify-between p-4 border-b">
        <div className="flex items-center gap-2">
          <Dumbbell className="h-6 w-6 text-primary" />
          <h1 className="text-xl font-bold">FitClub</h1>
        </div>
        <Sheet>
          <SheetTrigger asChild>
            <Button variant="ghost" size="icon">
              <Menu className="h-6 w-6" />
            </Button>
          </SheetTrigger>
          <SheetContent side="left">
            <div className="flex flex-col gap-6 mt-8">
              <Link to="#" className="flex items-center gap-3 text-lg font-medium">
                <User className="h-5 w-5" />
                Профиль
              </Link>
              <Link to="#" className="flex items-center gap-3 text-lg font-medium">
                <Calendar className="h-5 w-5" />
                Расписание
              </Link>
              <Link to="#" className="flex items-center gap-3 text-lg font-medium">
                <Dumbbell className="h-5 w-5" />
                Тренировки
              </Link>
              <Link to="#" className="flex items-center gap-3 text-lg font-medium">
                <CreditCard className="h-5 w-5" />
                Абонемент
              </Link>
              <Link to="#" className="flex items-center gap-3 text-lg font-medium">
                <BarChart className="h-5 w-5" />
                Прогресс
              </Link>
            </div>
          </SheetContent>
        </Sheet>
      </div>

      <div className="flex">
        {/* Desktop Sidebar */}
        <aside className="hidden md:flex flex-col w-64 border-r h-screen p-6 sticky top-0">
          <div className="flex items-center gap-2 mb-8">
            <Dumbbell className="h-6 w-6 text-primary" />
            <h1 className="text-xl font-bold">FitClub</h1>
          </div>
          <nav className="space-y-6 flex-1">
            <Link to="#" className="flex items-center gap-3 text-lg font-medium">
              <User className="h-5 w-5" />
              Профиль
            </Link>
            <Link to="#" className="flex items-center gap-3 text-lg font-medium">
              <Calendar className="h-5 w-5" />
              Расписание
            </Link>
            <Link to="#" className="flex items-center gap-3 text-lg font-medium">
              <Dumbbell className="h-5 w-5" />
              Тренировки
            </Link>
            <Link to="#" className="flex items-center gap-3 text-lg font-medium">
              <CreditCard className="h-5 w-5" />
              Абонемент
            </Link>
            <Link to="#" className="flex items-center gap-3 text-lg font-medium">
              <BarChart className="h-5 w-5" />
              Прогресс
            </Link>
          </nav>
          <div className="mt-auto pt-6 border-t">
            <div className="flex items-center gap-3">
              <Avatar>
                <AvatarImage src="/placeholder.svg?height=40&width=40" />
                <AvatarFallback>ИП</AvatarFallback>
              </Avatar>
              <div>
                <p className="font-medium">Иван Петров</p>
                <p className="text-sm text-muted-foreground">Премиум</p>
              </div>
            </div>
          </div>
        </aside>

        {/* Main Content */}
        <main className="flex-1 p-4 md:p-8">
          <div className="max-w-6xl mx-auto">
            <div className="flex flex-col md:flex-row md:items-center md:justify-between mb-8">
              <div>
                <h1 className="text-2xl md:text-3xl font-bold">Добро пожаловать, Иван!</h1>
                <p className="text-muted-foreground">Ваш фитнес-прогресс на этой неделе</p>
              </div>
              <Button className="mt-4 md:mt-0">Забронировать тренировку</Button>
            </div>

            {/* Stats Overview */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-8">
              <Card>
                <CardHeader className="pb-2">
                  <CardTitle className="text-sm font-medium">Посещения в этом месяце</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold">12/20</div>
                  <Progress value={60} className="h-2 mt-2" />
                </CardContent>
              </Card>
              <Card>
                <CardHeader className="pb-2">
                  <CardTitle className="text-sm font-medium">Активность</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold">8 часов</div>
                  <p className="text-xs text-muted-foreground mt-1">+2ч по сравнению с прошлой неделей</p>
                </CardContent>
              </Card>
              <Card>
                <CardHeader className="pb-2">
                  <CardTitle className="text-sm font-medium">Срок абонемента</CardTitle>
                </CardHeader>
                <CardContent>
                  <div className="text-2xl font-bold">45 дней</div>
                  <p className="text-xs text-muted-foreground mt-1">Истекает 30 апреля</p>
                </CardContent>
              </Card>
            </div>

            {/* Upcoming Classes */}
            <div className="mb-8">
              <h2 className="text-xl font-bold mb-4">Ближайшие занятия</h2>
              <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                <Card>
                  <CardContent className="p-0">
                    <div className="flex items-start p-4">
                      <div className="bg-primary/10 p-3 rounded-lg mr-4">
                        <Calendar className="h-6 w-6 text-primary" />
                      </div>
                      <div className="flex-1">
                        <div className="flex items-center justify-between">
                          <h3 className="font-semibold">Групповая тренировка</h3>
                          <Badge>Сегодня</Badge>
                        </div>
                        <p className="text-sm text-muted-foreground mt-1">18:00 - 19:00</p>
                        <p className="text-sm mt-2">Тренер: Алексей К.</p>
                      </div>
                    </div>
                  </CardContent>
                </Card>
                <Card>
                  <CardContent className="p-0">
                    <div className="flex items-start p-4">
                      <div className="bg-primary/10 p-3 rounded-lg mr-4">
                        <Dumbbell className="h-6 w-6 text-primary" />
                      </div>
                      <div className="flex-1">
                        <div className="flex items-center justify-between">
                          <h3 className="font-semibold">Персональная тренировка</h3>
                          <Badge variant="outline">Завтра</Badge>
                        </div>
                        <p className="text-sm text-muted-foreground mt-1">10:00 - 11:00</p>
                        <p className="text-sm mt-2">Тренер: Мария С.</p>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </div>
            </div>

            {/* Workout Progress */}
            <div>
              <h2 className="text-xl font-bold mb-4">Прогресс тренировок</h2>
              <Card>
                <CardHeader>
                  <CardTitle>Статистика за последний месяц</CardTitle>
                  <CardDescription>Отслеживайте свой прогресс</CardDescription>
                </CardHeader>
                <CardContent>
                  <div className="space-y-4">
                    <div>
                      <div className="flex items-center justify-between mb-1">
                        <span className="text-sm font-medium">Кардио</span>
                        <span className="text-sm font-medium">8 часов</span>
                      </div>
                      <Progress value={80} className="h-2" />
                    </div>
                    <div>
                      <div className="flex items-center justify-between mb-1">
                        <span className="text-sm font-medium">Силовые</span>
                        <span className="text-sm font-medium">6 часов</span>
                      </div>
                      <Progress value={60} className="h-2" />
                    </div>
                    <div>
                      <div className="flex items-center justify-between mb-1">
                        <span className="text-sm font-medium">Растяжка</span>
                        <span className="text-sm font-medium">3 часа</span>
                      </div>
                      <Progress value={30} className="h-2" />
                    </div>
                  </div>
                </CardContent>
              </Card>
            </div>
          </div>
        </main>
      </div>
    </div>
  )
}

