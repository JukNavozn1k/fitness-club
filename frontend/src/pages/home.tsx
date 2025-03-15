

import { Button } from "@/components/ui/button"
import { Card, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import { ChevronRight, Dumbbell, Users, Calendar, Award, Menu, X } from "lucide-react"
import { useState } from "react"
import {Link} from "react-router-dom"
function MobileMenu() {
  const [isOpen, setIsOpen] = useState(false)

  return (
    <div className="md:hidden">
      <Button variant="outline" size="icon" onClick={() => setIsOpen(!isOpen)}>
        <span className="sr-only">Меню</span>
        {isOpen ? <X className="h-6 w-6" /> : <Menu className="h-6 w-6" />}
      </Button>

      {isOpen && (
        <div className="fixed inset-0 top-16 z-50 bg-background shadow-lg">
          <div className="container flex flex-col py-6 gap-4 bg-background">
            <Link href="#" className="text-lg font-medium py-2 hover:text-primary" onClick={() => setIsOpen(false)}>
              Главная
            </Link>
            <Link
              href="#offerings"
              className="text-lg font-medium py-2 hover:text-primary"
              onClick={() => setIsOpen(false)}
            >
              Услуги
            </Link>
            <Link href="#" className="text-lg font-medium py-2 hover:text-primary" onClick={() => setIsOpen(false)}>
              Расписание
            </Link>
            <Link href="#" className="text-lg font-medium py-2 hover:text-primary" onClick={() => setIsOpen(false)}>
              О нас
            </Link>
            <Link href="#" className="text-lg font-medium py-2 hover:text-primary" onClick={() => setIsOpen(false)}>
              Контакты
            </Link>
            <div className="flex flex-col gap-2 mt-4">
              <Button asChild variant="outline">
                <Link href="/login">Войти</Link>
              </Button>
              <Button asChild>
                <Link href="/register">Регистрация</Link>
              </Button>
            </div>
          </div>
        </div>
      )}
    </div>
  )
}

export default function Home() {
  // This would eventually come from your admin panel/database
  const offerings = [
    {
      id: 1,
      title: "Персональные тренировки",
      description: "Индивидуальные занятия с профессиональным тренером",
      icon: Dumbbell,
      price: "от 1500₽",
    },
    {
      id: 2,
      title: "Групповые занятия",
      description: "Тренировки в группах по различным направлениям",
      icon: Users,
      price: "от 800₽",
    },
    {
      id: 3,
      title: "Абонементы",
      description: "Выгодные предложения для регулярных посещений",
      icon: Calendar,
      price: "от 3000₽",
    },
    {
      id: 4,
      title: "Специальные программы",
      description: "Программы для похудения, набора массы и реабилитации",
      icon: Award,
      price: "от 5000₽",
    },
  ]

  return (
    <div className="flex min-h-screen flex-col">
      <header className="sticky top-0 z-50 w-full border-b bg-background">
        <div className="container flex h-16 items-center justify-between">
          <div className="flex items-center gap-2 font-bold text-xl">
            <Dumbbell className="h-6 w-6" />
            <span>ФитнесКлуб</span>
          </div>
          <nav className="hidden md:flex gap-6 items-center">
            <Link href="#" className="text-sm font-medium hover:underline underline-offset-4">
              Главная
            </Link>
            <Link href="#offerings" className="text-sm font-medium hover:underline underline-offset-4">
              Услуги
            </Link>
            <Link href="#" className="text-sm font-medium hover:underline underline-offset-4">
              Расписание
            </Link>
            <Link href="#" className="text-sm font-medium hover:underline underline-offset-4">
              О нас
            </Link>
            <Link href="#" className="text-sm font-medium hover:underline underline-offset-4">
              Контакты
            </Link>
          </nav>
          <div className="flex items-center gap-4">
            <Button asChild variant="outline" size="sm" className="hidden md:flex">
              <Link href="/login">Войти</Link>
            </Button>
            <Button asChild size="sm" className="hidden md:flex">
              <Link href="/register">Регистрация</Link>
            </Button>
            <MobileMenu />
          </div>
        </div>
      </header>
      <main className="flex-1">
        <section className="w-full py-12 md:py-24 lg:py-32 bg-muted">
          <div className="container px-4 md:px-6">
            <div className="grid gap-6 lg:grid-cols-2 lg:gap-12 items-center">
              <div className="space-y-4">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-5xl xl:text-6xl/none">
                  Достигайте своих целей вместе с нами
                </h1>
                <p className="max-w-[600px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Современное оборудование, профессиональные тренеры и комфортная атмосфера для вашего идеального тела
                </p>
                <div className="flex flex-col gap-2 min-[400px]:flex-row">
                  <Button size="lg">Начать сейчас</Button>
                  <Button size="lg" variant="outline">
                    Узнать больше
                  </Button>
                </div>
              </div>
              <img
                src="/placeholder.svg?height=550&width=800"
                alt="Фитнес клуб"
                className="mx-auto aspect-video overflow-hidden rounded-xl object-cover object-center sm:w-full lg:order-last"
                width={550}
                height={310}
              />
            </div>
          </div>
        </section>
        <section id="offerings" className="w-full py-12 md:py-24 lg:py-32">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <div className="inline-block rounded-lg bg-muted px-3 py-1 text-sm">Наши услуги</div>
                <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight">Выберите подходящую программу</h2>
                <p className="max-w-[900px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Мы предлагаем широкий спектр услуг для достижения ваших фитнес-целей
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-4 mt-8">
              {offerings.map((offering) => (
                <Card key={offering.id} className="flex flex-col justify-between">
                  <CardHeader>
                    <div className="mb-2 w-fit rounded-md bg-primary/10 p-2 text-primary">
                      <offering.icon className="h-6 w-6" />
                    </div>
                    <CardTitle>{offering.title}</CardTitle>
                    <CardDescription>{offering.description}</CardDescription>
                  </CardHeader>
                  <CardFooter className="flex justify-between">
                    <p className="font-medium">{offering.price}</p>
                    <Button variant="ghost" size="sm" className="gap-1">
                      Подробнее <ChevronRight className="h-4 w-4" />
                    </Button>
                  </CardFooter>
                </Card>
              ))}
            </div>
            <div className="flex justify-center mt-10">
              <Button size="lg">Посмотреть все услуги</Button>
            </div>
          </div>
        </section>
        <section className="w-full py-12 md:py-24 lg:py-32 bg-muted">
          <div className="container px-4 md:px-6">
            <div className="grid gap-6 lg:grid-cols-2 lg:gap-12 items-center">
              <img
                src="/placeholder.svg?height=550&width=800"
                alt="Тренировка в фитнес клубе"
                className="mx-auto aspect-video overflow-hidden rounded-xl object-cover object-center sm:w-full"
                width={550}
                height={310}
              />
              <div className="space-y-4">
                <h2 className="text-3xl font-bold tracking-tighter md:text-4xl/tight">Почему выбирают нас</h2>
                <p className="max-w-[600px] text-muted-foreground md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Наш фитнес клуб предлагает не только тренировки, но и целую экосистему для вашего здоровья и красоты
                </p>
                <ul className="grid gap-4">
                  <li className="flex items-center gap-2">
                    <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary text-primary-foreground">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="h-4 w-4"
                      >
                        <polyline points="20 6 9 17 4 12" />
                      </svg>
                    </div>
                    <span>Современное оборудование от ведущих производителей</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary text-primary-foreground">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="h-4 w-4"
                      >
                        <polyline points="20 6 9 17 4 12" />
                      </svg>
                    </div>
                    <span>Команда сертифицированных тренеров с опытом работы</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary text-primary-foreground">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="h-4 w-4"
                      >
                        <polyline points="20 6 9 17 4 12" />
                      </svg>
                    </div>
                    <span>Просторные залы и комфортные раздевалки</span>
                  </li>
                  <li className="flex items-center gap-2">
                    <div className="flex h-8 w-8 items-center justify-center rounded-full bg-primary text-primary-foreground">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        width="24"
                        height="24"
                        viewBox="0 0 24 24"
                        fill="none"
                        stroke="currentColor"
                        strokeWidth="2"
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        className="h-4 w-4"
                      >
                        <polyline points="20 6 9 17 4 12" />
                      </svg>
                    </div>
                    <span>Гибкая система абонементов и специальные предложения</span>
                  </li>
                </ul>
                <div className="flex flex-col gap-2 min-[400px]:flex-row">
                  <Button size="lg">Записаться на пробное занятие</Button>
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
      <footer className="w-full border-t py-6 md:py-0">
        <div className="container flex flex-col items-center justify-between gap-4 md:h-24 md:flex-row">
          <p className="text-center text-sm leading-loose text-muted-foreground md:text-left">
            © 2025 ФитнесКлуб. Все права защищены.
          </p>
          <div className="flex gap-4">
            <Link href="#" className="text-sm font-medium hover:underline underline-offset-4">
              Политика конфиденциальности
            </Link>
            <Link href="#" className="text-sm font-medium hover:underline underline-offset-4">
              Условия использования
            </Link>
          </div>
        </div>
      </footer>
    </div>
  )
}

