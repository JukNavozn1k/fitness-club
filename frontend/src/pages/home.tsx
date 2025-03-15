import { Input } from "@/components/ui/input"
import { Label } from "@/components/ui/label"
import {Link} from "react-router-dom"
import { Button } from "@/components/ui/button"
import { Dumbbell, Users, Clock, Award, ChevronRight, Instagram, Facebook, Twitter } from "lucide-react"

export default function Home() {
  return (
    <div className="flex flex-col min-h-screen">
      {/* Header */}
      <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
        <div className="container flex h-16 items-center justify-between">
          <div className="flex items-center gap-2">
            <Dumbbell className="h-6 w-6" />
            <span className="text-xl font-bold">FitClub</span>
          </div>
          <nav className="hidden md:flex gap-6">
            <Link to="#" className="text-sm font-medium hover:text-primary">
              Home
            </Link>
            <Link to="#about" className="text-sm font-medium hover:text-primary">
              About
            </Link>
            <Link to="#classes" className="text-sm font-medium hover:text-primary">
              Classes
            </Link>
            <Link to="#trainers" className="text-sm font-medium hover:text-primary">
              Trainers
            </Link>
            <Link to="#pricing" className="text-sm font-medium hover:text-primary">
              Pricing
            </Link>
            <Link to="#contact" className="text-sm font-medium hover:text-primary">
              Contact
            </Link>
          </nav>
          <div className="flex items-center gap-4">
            <Button variant="outline" className="hidden md:flex">
              Log In
            </Button>
            <Button>Join Now</Button>
          </div>
        </div>
      </header>

      <main className="flex-1">
        {/* Hero Section */}
        <section className="relative py-20 md:py-32 bg-gradient-to-r from-gray-900 to-gray-800 text-white">
          <div className="container flex flex-col md:flex-row items-center gap-8">
            <div className="md:w-1/2 space-y-6">
              <h1 className="text-4xl md:text-6xl font-bold leading-tight">
                Трансформируйте свое тело, измените свою жизнь
              </h1>
              <p className="text-lg md:text-xl text-gray-300">
                Современный фитнес-клуб с лучшим оборудованием и профессиональными тренерами для достижения ваших целей.
              </p>
              <div className="flex flex-col sm:flex-row gap-4">
                <Button size="lg" className="bg-primary hover:bg-primary/90">
                  Начать сейчас
                </Button>
                <Button size="lg" variant="outline" className="border-white text-white hover:bg-white hover:text-black">
                  Узнать больше
                </Button>
              </div>
            </div>
            <div className="md:w-1/2">
              <img
                src="/placeholder.svg?height=600&width=600"
                alt="Fitness training"
                className="rounded-lg shadow-2xl"
              />
            </div>
          </div>
          <div className="absolute bottom-0 left-0 right-0 h-16 bg-gradient-to-t from-background to-transparent" />
        </section>

        {/* Features Section */}
        <section id="about" className="py-20 bg-background">
          <div className="container">
            <div className="text-center mb-16">
              <h2 className="text-3xl md:text-4xl font-bold mb-4">Почему выбирают нас</h2>
              <p className="text-muted-foreground max-w-2xl mx-auto">
                Мы предлагаем лучшие условия для тренировок и достижения ваших фитнес-целей
              </p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              <div className="bg-card p-8 rounded-lg shadow-sm border">
                <div className="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mb-6">
                  <Dumbbell className="h-6 w-6 text-primary" />
                </div>
                <h3 className="text-xl font-bold mb-3">Современное оборудование</h3>
                <p className="text-muted-foreground">
                  Новейшие тренажеры и оборудование для эффективных тренировок любого уровня сложности.
                </p>
              </div>
              <div className="bg-card p-8 rounded-lg shadow-sm border">
                <div className="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mb-6">
                  <Users className="h-6 w-6 text-primary" />
                </div>
                <h3 className="text-xl font-bold mb-3">Профессиональные тренеры</h3>
                <p className="text-muted-foreground">
                  Сертифицированные тренеры с богатым опытом помогут вам достичь желаемых результатов.
                </p>
              </div>
              <div className="bg-card p-8 rounded-lg shadow-sm border">
                <div className="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mb-6">
                  <Clock className="h-6 w-6 text-primary" />
                </div>
                <h3 className="text-xl font-bold mb-3">Гибкий график</h3>
                <p className="text-muted-foreground">
                  Мы работаем 24/7, чтобы вы могли тренироваться в удобное для вас время.
                </p>
              </div>
            </div>
          </div>
        </section>

        {/* Classes Section */}
        <section id="classes" className="py-20 bg-muted/50">
          <div className="container">
            <div className="text-center mb-16">
              <h2 className="text-3xl md:text-4xl font-bold mb-4">Наши программы</h2>
              <p className="text-muted-foreground max-w-2xl mx-auto">Выберите программу, которая подходит именно вам</p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
              {[
                {
                  title: "Силовые тренировки",
                  description: "Развитие силы и наращивание мышечной массы под руководством опытных тренеров.",
                  image: "/placeholder.svg?height=300&width=400",
                },
                {
                  title: "Кардио",
                  description: "Интенсивные кардио-тренировки для улучшения выносливости и сжигания калорий.",
                  image: "/placeholder.svg?height=300&width=400",
                },
                {
                  title: "Йога",
                  description: "Улучшение гибкости, баланса и снятие стресса через практику йоги.",
                  image: "/placeholder.svg?height=300&width=400",
                },
                {
                  title: "Функциональный тренинг",
                  description: "Комплексные упражнения для развития всех групп мышц и улучшения координации.",
                  image: "/placeholder.svg?height=300&width=400",
                },
                {
                  title: "Групповые занятия",
                  description: "Мотивирующие групповые тренировки под руководством энергичных инструкторов.",
                  image: "/placeholder.svg?height=300&width=400",
                },
                {
                  title: "Персональные тренировки",
                  description: "Индивидуальный подход и программа, разработанная специально для ваших целей.",
                  image: "/placeholder.svg?height=300&width=400",
                },
              ].map((cls, index) => (
                <div key={index} className="group relative overflow-hidden rounded-lg shadow-md">
                  <img
                    src={cls.image || "/placeholder.svg"}
                    alt={cls.title}
                    className="w-full h-64 object-cover transition-transform duration-300 group-hover:scale-105"
                  />
                  <div className="absolute inset-0 bg-gradient-to-t from-black/80 to-transparent flex flex-col justify-end p-6">
                    <h3 className="text-xl font-bold text-white mb-2">{cls.title}</h3>
                    <p className="text-gray-200 text-sm mb-4">{cls.description}</p>
                    <Button
                      variant="outline"
                      className="w-full border-white text-white hover:bg-white hover:text-black"
                    >
                      Подробнее
                    </Button>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Trainers Section */}
        <section id="trainers" className="py-20 bg-background">
          <div className="container">
            <div className="text-center mb-16">
              <h2 className="text-3xl md:text-4xl font-bold mb-4">Наши тренеры</h2>
              <p className="text-muted-foreground max-w-2xl mx-auto">
                Профессионалы, которые помогут вам достичь ваших целей
              </p>
            </div>
            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8">
              {[
                {
                  name: "Алексей Петров",
                  role: "Силовой тренинг",
                  image: "/placeholder.svg?height=400&width=300",
                },
                {
                  name: "Мария Иванова",
                  role: "Йога и пилатес",
                  image: "/placeholder.svg?height=400&width=300",
                },
                {
                  name: "Дмитрий Сидоров",
                  role: "Функциональный тренинг",
                  image: "/placeholder.svg?height=400&width=300",
                },
                {
                  name: "Елена Смирнова",
                  role: "Кардио и групповые занятия",
                  image: "/placeholder.svg?height=400&width=300",
                },
              ].map((trainer, index) => (
                <div key={index} className="bg-card rounded-lg overflow-hidden shadow-md group">
                  <div className="relative overflow-hidden">
                    <img
                      src={trainer.image || "/placeholder.svg"}
                      alt={trainer.name}
                      className="w-full h-80 object-cover transition-transform duration-300 group-hover:scale-105"
                    />
                    <div className="absolute inset-0 bg-black/40 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center gap-4">
                      <Button
                        size="icon"
                        variant="ghost"
                        className="rounded-full text-white hover:text-white hover:bg-primary"
                      >
                        <Instagram className="h-5 w-5" />
                      </Button>
                      <Button
                        size="icon"
                        variant="ghost"
                        className="rounded-full text-white hover:text-white hover:bg-primary"
                      >
                        <Facebook className="h-5 w-5" />
                      </Button>
                      <Button
                        size="icon"
                        variant="ghost"
                        className="rounded-full text-white hover:text-white hover:bg-primary"
                      >
                        <Twitter className="h-5 w-5" />
                      </Button>
                    </div>
                  </div>
                  <div className="p-6">
                    <h3 className="text-xl font-bold">{trainer.name}</h3>
                    <p className="text-muted-foreground">{trainer.role}</p>
                  </div>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* Pricing Section */}
        <section id="pricing" className="py-20 bg-muted/50">
          <div className="container">
            <div className="text-center mb-16">
              <h2 className="text-3xl md:text-4xl font-bold mb-4">Тарифы</h2>
              <p className="text-muted-foreground max-w-2xl mx-auto">Выберите подходящий тариф для ваших тренировок</p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              <div className="bg-card rounded-lg shadow-md overflow-hidden border">
                <div className="p-8 border-b">
                  <h3 className="text-2xl font-bold mb-2">Базовый</h3>
                  <div className="flex items-baseline mb-4">
                    <span className="text-4xl font-bold">2,500₽</span>
                    <span className="text-muted-foreground ml-2">/месяц</span>
                  </div>
                  <p className="text-muted-foreground">Идеально для начинающих</p>
                </div>
                <div className="p-8">
                  <ul className="space-y-4">
                    <li className="flex items-center">
                      <ChevronRight className="h-5 w-5 text-primary mr-2" />
                      <span>Доступ к тренажерному залу</span>
                    </li>
                    <li className="flex items-center">
                      <ChevronRight className="h-5 w-5 text-primary mr-2" />
                      <span>Базовые групповые занятия</span>
                    </li>
                    <li className="flex items-center">
                      <ChevronRight className="h-5 w-5 text-primary mr-2" />
                      <span>Доступ с 8:00 до 22:00</span>
                    </li>
                  </ul>
                  <Button className="w-full mt-8">Выбрать</Button>
                </div>
              </div>
              <div className="bg-card rounded-lg shadow-md overflow-hidden border border-primary relative">
                <div className="absolute top-0 right-0 bg-primary text-white px-4 py-1 text-sm font-medium">
                  Популярный
                </div>
                <div className="p-8 border-b">
                  <h3 className="text-2xl font-bold mb-2">Стандарт</h3>
                  <div className="flex items-baseline mb-4">
                    <span className="text-4xl font-bold">4,500₽</span>
                    <span className="text-muted-foreground ml-2">/месяц</span>
                  </div>
                  <p className="text-muted-foreground">Для регулярных тренировок</p>
                </div>
                <div className="p-8">
                  <ul className="space-y-4">
                    <li className="flex items-center">
                      <ChevronRight className="h-5 w-5 text-primary mr-2" />
                      <span>Все включено в Базовый</span>
                    </li>
                    <li className="flex items-center">
                      <ChevronRight className="h-5 w-5 text-primary mr-2" />
                      <span>Все групповые занятия</span>
                    </li>
                    <li className="flex items-center">
                      <ChevronRight className="h-5 w-5 text-primary mr-2" />
                      <span>1 персональная тренировка</span>
                    </li>
                    <li className="flex items-center">
                      <ChevronRight className="h-5 w-5 text-primary mr-2" />
                      <span>Доступ 24/7</span>
                    </li>
                  </ul>
                  <Button className="w-full mt-8">Выбрать</Button>
                </div>
              </div>
              <div className="bg-card rounded-lg shadow-md overflow-hidden border">
                <div className="p-8 border-b">
                  <h3 className="text-2xl font-bold mb-2">Премиум</h3>
                  <div className="flex items-baseline mb-4">
                    <span className="text-4xl font-bold">7,500₽</span>
                    <span className="text-muted-foreground ml-2">/месяц</span>
                  </div>
                  <p className="text-muted-foreground">Максимальные результаты</p>
                </div>
                <div className="p-8">
                  <ul className="space-y-4">
                    <li className="flex items-center">
                      <ChevronRight className="h-5 w-5 text-primary mr-2" />
                      <span>Все включено в Стандарт</span>
                    </li>
                    <li className="flex items-center">
                      <ChevronRight className="h-5 w-5 text-primary mr-2" />
                      <span>4 персональные тренировки</span>
                    </li>
                    <li className="flex items-center">
                      <ChevronRight className="h-5 w-5 text-primary mr-2" />
                      <span>Составление питания</span>
                    </li>
                    <li className="flex items-center">
                      <ChevronRight className="h-5 w-5 text-primary mr-2" />
                      <span>Доступ в VIP-зону</span>
                    </li>
                  </ul>
                  <Button className="w-full mt-8">Выбрать</Button>
                </div>
              </div>
            </div>
          </div>
        </section>

        {/* Testimonials */}
        <section className="py-20 bg-background">
          <div className="container">
            <div className="text-center mb-16">
              <h2 className="text-3xl md:text-4xl font-bold mb-4">Отзывы клиентов</h2>
              <p className="text-muted-foreground max-w-2xl mx-auto">Что говорят о нас наши клиенты</p>
            </div>
            <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
              {[
                {
                  name: "Анна К.",
                  text: "Занимаюсь в этом клубе уже год. Отличное оборудование и внимательные тренеры. Достигла всех поставленных целей и продолжаю совершенствоваться!",
                  image: "/placeholder.svg?height=100&width=100",
                },
                {
                  name: "Сергей М.",
                  text: "Перепробовал много фитнес-клубов, но остановился на этом. Здесь действительно помогают достичь результатов, а не просто продают абонементы.",
                  image: "/placeholder.svg?height=100&width=100",
                },
                {
                  name: "Екатерина Д.",
                  text: "Групповые занятия просто супер! Тренеры мотивируют и помогают выкладываться на 100%. За полгода сбросила 15 кг и чувствую себя отлично!",
                  image: "/placeholder.svg?height=100&width=100",
                },
              ].map((testimonial, index) => (
                <div key={index} className="bg-card p-8 rounded-lg shadow-sm border">
                  <div className="flex items-center mb-6">
                    <img
                      src={testimonial.image || "/placeholder.svg"}
                      alt={testimonial.name}
                      className="w-12 h-12 rounded-full mr-4 object-cover"
                    />
                    <div>
                      <h4 className="font-bold">{testimonial.name}</h4>
                      <div className="flex text-yellow-500">
                        {[...Array(5)].map((_, i) => (
                          <Award key={i} className="h-4 w-4" />
                        ))}
                      </div>
                    </div>
                  </div>
                  <p className="text-muted-foreground italic">"{testimonial.text}"</p>
                </div>
              ))}
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section className="py-20 bg-primary text-primary-foreground">
          <div className="container text-center">
            <h2 className="text-3xl md:text-4xl font-bold mb-6">Готовы начать свой путь к здоровью?</h2>
            <p className="text-lg mb-8 max-w-2xl mx-auto opacity-90">
              Присоединяйтесь к нам сегодня и получите бесплатную консультацию с тренером
            </p>
            <div className="flex flex-col sm:flex-row gap-4 justify-center">
              <Button size="lg" variant="secondary">
                Записаться на пробную тренировку
              </Button>
              <Button
                size="lg"
                variant="outline"
                className="border-primary-foreground text-primary-foreground hover:bg-primary-foreground hover:text-primary"
              >
                Связаться с нами
              </Button>
            </div>
          </div>
        </section>

        {/* Contact Section */}
        <section id="contact" className="py-20 bg-muted/50">
          <div className="container">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-12">
              <div>
                <h2 className="text-3xl font-bold mb-6">Свяжитесь с нами</h2>
                <p className="text-muted-foreground mb-8">У вас есть вопросы? Мы с радостью на них ответим!</p>
                <div className="space-y-4">
                  <div className="flex items-start">
                    <div className="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mr-4">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-5 w-5 text-primary"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"
                        />
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"
                        />
                      </svg>
                    </div>
                    <div>
                      <h3 className="text-lg font-medium">Адрес</h3>
                      <p className="text-muted-foreground">ул. Спортивная, 123, Москва</p>
                    </div>
                  </div>
                  <div className="flex items-start">
                    <div className="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mr-4">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-5 w-5 text-primary"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"
                        />
                      </svg>
                    </div>
                    <div>
                      <h3 className="text-lg font-medium">Телефон</h3>
                      <p className="text-muted-foreground">+7 (495) 123-45-67</p>
                    </div>
                  </div>
                  <div className="flex items-start">
                    <div className="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mr-4">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-5 w-5 text-primary"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"
                        />
                      </svg>
                    </div>
                    <div>
                      <h3 className="text-lg font-medium">Email</h3>
                      <p className="text-muted-foreground">info@fitclub.ru</p>
                    </div>
                  </div>
                  <div className="flex items-start">
                    <div className="w-12 h-12 bg-primary/10 rounded-full flex items-center justify-center mr-4">
                      <svg
                        xmlns="http://www.w3.org/2000/svg"
                        className="h-5 w-5 text-primary"
                        fill="none"
                        viewBox="0 0 24 24"
                        stroke="currentColor"
                      >
                        <path
                          strokeLinecap="round"
                          strokeLinejoin="round"
                          strokeWidth={2}
                          d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                        />
                      </svg>
                    </div>
                    <div>
                      <h3 className="text-lg font-medium">Часы работы</h3>
                      <p className="text-muted-foreground">Пн-Вс: 24/7</p>
                    </div>
                  </div>
                </div>
                <div className="flex gap-4 mt-8">
                  <Button size="icon" variant="outline">
                    <Facebook className="h-5 w-5" />
                  </Button>
                  <Button size="icon" variant="outline">
                    <Instagram className="h-5 w-5" />
                  </Button>
                  <Button size="icon" variant="outline">
                    <Twitter className="h-5 w-5" />
                  </Button>
                </div>
              </div>
              <div className="bg-card p-8 rounded-lg shadow-sm border">
                <h3 className="text-xl font-bold mb-6">Отправьте нам сообщение</h3>
                <form className="space-y-4">
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                    <div className="space-y-2">
                      <Label htmlFor="name">Имя</Label>
                      <Input id="name" placeholder="Ваше имя" />
                    </div>
                    <div className="space-y-2">
                      <Label htmlFor="email">Email</Label>
                      <Input id="email" type="email" placeholder="Ваш email" />
                    </div>
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="phone">Телефон</Label>
                    <Input id="phone" placeholder="+7 (___) ___-__-__" />
                  </div>
                  <div className="space-y-2">
                    <Label htmlFor="message">Сообщение</Label>
                    <textarea
                      id="message"
                      rows={4}
                      className="w-full min-h-[120px] rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50"
                      placeholder="Ваше сообщение"
                    ></textarea>
                  </div>
                  <Button className="w-full">Отправить</Button>
                </form>
              </div>
            </div>
          </div>
        </section>
      </main>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-300 py-12">
        <div className="container">
          <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
            <div>
              <div className="flex items-center gap-2 mb-6">
                <Dumbbell className="h-6 w-6 text-primary" />
                <span className="text-xl font-bold text-white">FitClub</span>
              </div>
              <p className="mb-6">
                Современный фитнес-клуб с лучшим оборудованием и профессиональными тренерами для достижения ваших целей.
              </p>
              <div className="flex gap-4">
                <Button size="icon" variant="ghost" className="text-gray-300 hover:text-white hover:bg-primary/20">
                  <Facebook className="h-5 w-5" />
                </Button>
                <Button size="icon" variant="ghost" className="text-gray-300 hover:text-white hover:bg-primary/20">
                  <Instagram className="h-5 w-5" />
                </Button>
                <Button size="icon" variant="ghost" className="text-gray-300 hover:text-white hover:bg-primary/20">
                  <Twitter className="h-5 w-5" />
                </Button>
              </div>
            </div>
            <div>
              <h3 className="text-lg font-bold text-white mb-6">Быстрые ссылки</h3>
              <ul className="space-y-3">
                <li>
                  <Link to="#" className="hover:text-primary transition-colors">
                    Главная
                  </Link>
                </li>
                <li>
                  <Link to="#about" className="hover:text-primary transition-colors">
                    О нас
                  </Link>
                </li>
                <li>
                  <Link to="#classes" className="hover:text-primary transition-colors">
                    Программы
                  </Link>
                </li>
                <li>
                  <Link to="#trainers" className="hover:text-primary transition-colors">
                    Тренеры
                  </Link>
                </li>
                <li>
                  <Link to="#pricing" className="hover:text-primary transition-colors">
                    Тарифы
                  </Link>
                </li>
                <li>
                  <Link to="#contact" className="hover:text-primary transition-colors">
                    Контакты
                  </Link>
                </li>
              </ul>
            </div>
            <div>
              <h3 className="text-lg font-bold text-white mb-6">Программы</h3>
              <ul className="space-y-3">
                <li>
                  <Link to="#" className="hover:text-primary transition-colors">
                    Силовые тренировки
                  </Link>
                </li>
                <li>
                  <Link to="#" className="hover:text-primary transition-colors">
                    Кардио
                  </Link>
                </li>
                <li>
                  <Link to="#" className="hover:text-primary transition-colors">
                    Йога
                  </Link>
                </li>
                <li>
                  <Link to="#" className="hover:text-primary transition-colors">
                    Функциональный тренинг
                  </Link>
                </li>
                <li>
                  <Link to="#" className="hover:text-primary transition-colors">
                    Групповые занятия
                  </Link>
                </li>
                <li>
                  <Link to="#" className="hover:text-primary transition-colors">
                    Персональные тренировки
                  </Link>
                </li>
              </ul>
            </div>
            <div>
              <h3 className="text-lg font-bold text-white mb-6">Подписка</h3>
              <p className="mb-4">Подпишитесь на нашу рассылку, чтобы получать новости и специальные предложения</p>
              <div className="flex gap-2">
                <Input placeholder="Ваш email" className="bg-gray-800 border-gray-700" />
                <Button>Подписаться</Button>
              </div>
            </div>
          </div>
          <div className="border-t border-gray-800 mt-12 pt-8 text-center">
            <p>&copy; {new Date().getFullYear()} FitClub. Все права защищены.</p>
          </div>
        </div>
      </footer>
    </div>
  )
}

