import { Dumbbell, Users, Calendar, Award, MapPin, Phone, Mail, Clock } from "lucide-react"
import Sidebar from "@/components/ui/Sidebar"
import MobileNavbar from "@/components/ui/navbar"
export default function Home() {
  return (
    <div className="flex min-h-screen bg-background">
      {/* Sidebar for desktop */}
      <Sidebar />

      {/* Main content */}
      <main className="flex-1 pb-16 md:pb-0 md:ml-[var(--sidebar-width,256px)] transition-all duration-200">
        {/* Hero Section */}
        <section className="relative h-[500px] w-full bg-cover bg-center" style={{ backgroundImage: "url('/placeholder.svg?height=500&width=1200')" }}>
          <div className="absolute inset-0 bg-black/50 flex flex-col items-center justify-center text-white p-4 text-center">
            <h1 className="text-4xl md:text-6xl font-bold mb-4">POWER FITNESS</h1>
            <p className="text-xl md:text-2xl mb-8">Трансформируйте свое тело. Измените свою жизнь.</p>
            <button className="bg-primary hover:bg-primary/90 text-white font-bold py-3 px-8 rounded-full text-lg">
              Начать сейчас
            </button>
          </div>
        </section>

        {/* Features Section */}
        <section className="py-16 px-4 md:px-8">
          <h2 className="text-3xl font-bold text-center mb-12">Наши услуги</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            <FeatureCard
              icon={<Dumbbell className="h-10 w-10" />}
              title="Современное оборудование"
              description="Тренажерный зал оснащен новейшим оборудованием для эффективных тренировок."
            />
            <FeatureCard
              icon={<Users className="h-10 w-10" />}
              title="Групповые занятия"
              description="Разнообразные групповые программы для всех уровней подготовки."
            />
            <FeatureCard
              icon={<Calendar className="h-10 w-10" />}
              title="Персональные тренировки"
              description="Индивидуальный подход и программа тренировок от профессиональных тренеров."
            />
            <FeatureCard
              icon={<Award className="h-10 w-10" />}
              title="Квалифицированные тренеры"
              description="Наши тренеры имеют сертификаты и богатый опыт работы."
            />
            <FeatureCard
              icon={<Clock className="h-10 w-10" />}
              title="Гибкий график"
              description="Мы работаем 7 дней в неделю с раннего утра до позднего вечера."
            />
            <FeatureCard
              icon={<MapPin className="h-10 w-10" />}
              title="Удобное расположение"
              description="Фитнес-клуб находится в центре города с удобной транспортной доступностью."
            />
          </div>
        </section>

        {/* Membership Section */}
        <section className="py-16 px-4 md:px-8 bg-muted">
          <h2 className="text-3xl font-bold text-center mb-12">Абонементы</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <MembershipCard
              title="Базовый"
              price="2,500₽"
              period="в месяц"
              features={["Доступ к тренажерному залу", "Базовые групповые занятия", "Шкафчик для хранения вещей"]}
              buttonText="Выбрать"
              highlighted={false}
            />
            <MembershipCard
              title="Стандарт"
              price="4,000₽"
              period="в месяц"
              features={[
                "Все включено в Базовый",
                "Все групповые занятия",
                "1 персональная тренировка",
                "Сауна и душевые",
              ]}
              buttonText="Выбрать"
              highlighted={true}
            />
            <MembershipCard
              title="Премиум"
              price="6,500₽"
              period="в месяц"
              features={[
                "Все включено в Стандарт",
                "3 персональные тренировки",
                "Составление программы питания",
                "Приоритетная запись на занятия",
                "VIP-раздевалка",
              ]}
              buttonText="Выбрать"
              highlighted={false}
            />
          </div>
        </section>

        {/* Trainers Section */}
        <section className="py-16 px-4 md:px-8">
          <h2 className="text-3xl font-bold text-center mb-12">Наши тренеры</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
            <TrainerCard
              image="/placeholder.svg?height=300&width=300"
              name="Александр Петров"
              specialty="Силовые тренировки"
            />
            <TrainerCard
              image="/placeholder.svg?height=300&width=300"
              name="Елена Смирнова"
              specialty="Йога, Пилатес"
            />
            <TrainerCard image="/placeholder.svg?height=300&width=300" name="Дмитрий Иванов" specialty="Кроссфит" />
            <TrainerCard
              image="/placeholder.svg?height=300&width=300"
              name="Ольга Козлова"
              specialty="Функциональный тренинг"
            />
          </div>
        </section>

        {/* Testimonials */}
        <section className="py-16 px-4 md:px-8 bg-muted">
          <h2 className="text-3xl font-bold text-center mb-12">Отзывы клиентов</h2>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-8">
            <TestimonialCard
              quote="Занимаюсь в клубе уже год. Отличные тренеры и атмосфера. Результаты превзошли все ожидания!"
              author="Мария К."
              role="Клиент с 2022 года"
            />
            <TestimonialCard
              quote="Персональные тренировки с Александром полностью изменили мой подход к фитнесу. Рекомендую всем!"
              author="Игорь Л."
              role="Клиент с 2021 года"
            />
            <TestimonialCard
              quote="Удобное расположение, чистота и профессионализм персонала. Лучший фитнес-клуб в городе!"
              author="Анна С."
              role="Клиент с 2023 года"
            />
          </div>
        </section>

        {/* Contact Section */}
        <section className="py-16 px-4 md:px-8">
          <h2 className="text-3xl font-bold text-center mb-12">Контакты</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div className="bg-card rounded-lg p-6 shadow-md">
              <h3 className="text-2xl font-bold mb-4">Свяжитесь с нами</h3>
              <div className="space-y-4">
                <div className="flex items-center">
                  <Phone className="h-5 w-5 mr-3 text-primary" />
                  <span>+7 (123) 456-78-90</span>
                </div>
                <div className="flex items-center">
                  <Mail className="h-5 w-5 mr-3 text-primary" />
                  <span>info@powerfitness.ru</span>
                </div>
                <div className="flex items-center">
                  <MapPin className="h-5 w-5 mr-3 text-primary" />
                  <span>ул. Спортивная, 123, Москва</span>
                </div>
                <div className="flex items-center">
                  <Clock className="h-5 w-5 mr-3 text-primary" />
                  <span>Пн-Пт: 6:00 - 23:00, Сб-Вс: 8:00 - 22:00</span>
                </div>
              </div>
            </div>
            <div className="bg-card rounded-lg p-6 shadow-md">
              <h3 className="text-2xl font-bold mb-4">Запишитесь на пробное занятие</h3>
              <form className="space-y-4">
                <div>
                  <label htmlFor="name" className="block mb-1">
                    Имя
                  </label>
                  <input type="text" id="name" className="w-full p-2 border rounded-md" placeholder="Ваше имя" />
                </div>
                <div>
                  <label htmlFor="phone" className="block mb-1">
                    Телефон
                  </label>
                  <input
                    type="tel"
                    id="phone"
                    className="w-full p-2 border rounded-md"
                    placeholder="+7 (___) ___-__-__"
                  />
                </div>
                <div>
                  <label htmlFor="message" className="block mb-1">
                    Сообщение
                  </label>
                  <textarea
                    id="message"
                    rows={3}
                    className="w-full p-2 border rounded-md"
                    placeholder="Ваше сообщение"
                  ></textarea>
                </div>
                <button
                  type="submit"
                  className="bg-primary hover:bg-primary/90 text-white font-bold py-2 px-4 rounded-md w-full"
                >
                  Отправить
                </button>
              </form>
            </div>
          </div>
        </section>

        {/* Footer */}
        <footer className="bg-card text-card-foreground py-8 px-4 md:px-8">
          <div className="container mx-auto">
            <div className="grid grid-cols-1 md:grid-cols-4 gap-8">
              <div>
                <h3 className="text-xl font-bold mb-4">POWER FITNESS</h3>
                <p className="mb-4">Ваш путь к идеальной форме начинается здесь.</p>
              </div>
              <div>
                <h3 className="text-xl font-bold mb-4">Услуги</h3>
                <ul className="space-y-2">
                  <li>Тренажерный зал</li>
                  <li>Групповые занятия</li>
                  <li>Персональные тренировки</li>
                  <li>Фитнес-бар</li>
                </ul>
              </div>
              <div>
                <h3 className="text-xl font-bold mb-4">Часы работы</h3>
                <ul className="space-y-2">
                  <li>Понедельник - Пятница: 6:00 - 23:00</li>
                  <li>Суббота - Воскресенье: 8:00 - 22:00</li>
                </ul>
              </div>
              <div>
                <h3 className="text-xl font-bold mb-4">Контакты</h3>
                <ul className="space-y-2">
                  <li>ул. Спортивная, 123, Москва</li>
                  <li>+7 (123) 456-78-90</li>
                  <li>info@powerfitness.ru</li>
                </ul>
              </div>
            </div>
            <div className="border-t border-border mt-8 pt-8 text-center">
              <p>&copy; {new Date().getFullYear()} POWER FITNESS. Все права защищены.</p>
            </div>
          </div>
        </footer>
      </main>

      {/* Mobile Navigation */}
      <MobileNavbar />
    </div>
  )
}

// Component for feature cards
function FeatureCard({ icon, title, description }) {
  return (
    <div className="bg-card rounded-lg p-6 shadow-md flex flex-col items-center text-center">
      <div className="text-primary mb-4">{icon}</div>
      <h3 className="text-xl font-bold mb-2">{title}</h3>
      <p className="text-muted-foreground">{description}</p>
    </div>
  )
}

// Component for membership cards
function MembershipCard({ title, price, period, features, buttonText, highlighted }) {
  return (
    <div
      className={`${
        highlighted ? "bg-primary text-white" : "bg-card text-card-foreground"
      } p-6 rounded-lg shadow-md`}
    >
      <h3 className="text-2xl font-bold mb-4">{title}</h3>
      <p className="text-2xl font-semibold mb-4">
        {price} <span className="text-lg">/{period}</span>
      </p>
      <ul className="space-y-2 mb-4">
        {features.map((feature, index) => (
          <li key={index}>{feature}</li>
        ))}
      </ul>
      <button
        className={`${
          highlighted ? "bg-white text-primary" : "bg-primary text-white"
        } font-bold py-2 px-4 rounded-md w-full`}
      >
        {buttonText}
      </button>
    </div>
  )
}

// Component for trainer cards
function TrainerCard({ image, name, specialty }) {
  return (
    <div className="bg-card rounded-lg p-6 shadow-md text-center">
      <img src={image} alt={name} className="w-full h-56 object-cover rounded-lg mb-4" />
      <h3 className="text-xl font-bold mb-2">{name}</h3>
      <p className="text-muted-foreground">{specialty}</p>
    </div>
  )
}

// Component for testimonials
function TestimonialCard({ quote, author, role }) {
  return (
    <div className="bg-card rounded-lg p-6 shadow-md">
      <p className="text-muted-foreground mb-4">"{quote}"</p>
      <p className="font-semibold">{author}</p>
      <p className="text-muted-foreground">{role}</p>
    </div>
  )
}
