"use client"

import { useState, useEffect } from "react"
import { Link, useLocation } from "react-router-dom" // Используем React Router Link
import { Home, Dumbbell, Users, Calendar, Clock, Info, Phone } from "lucide-react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"

export default function Sidebar() {
  const location = useLocation()
  const currentPath = location.pathname.substring(1) || "home"
  const [sidebarWidth, setSidebarWidth] = useState(256)

  // Определяем, показывать ли текст или только иконки
  const showText = sidebarWidth > 120

  // Обновляем CSS переменную при изменении ширины
  useEffect(() => {
    document.documentElement.style.setProperty("--sidebar-width", `${sidebarWidth}px`)
  }, [sidebarWidth])

  const menuItems = [
    { id: "home", label: "Главная", icon: <Home className="h-5 w-5" /> },
    { id: "services", label: "Услуги", icon: <Dumbbell className="h-5 w-5" /> },
    { id: "trainers", label: "Тренеры", icon: <Users className="h-5 w-5" /> },
    { id: "schedule", label: "Расписание", icon: <Calendar className="h-5 w-5" /> },
    { id: "membership", label: "Абонементы", icon: <Clock className="h-5 w-5" /> },
    { id: "about", label: "О нас", icon: <Info className="h-5 w-5" /> },
    { id: "contact", label: "Контакты", icon: <Phone className="h-5 w-5" /> },
  ]

  // Функция для начала перетаскивания боковой панели
  const startResize = (mouseDownEvent: React.MouseEvent<HTMLDivElement>) => {
    mouseDownEvent.preventDefault()

    const startWidth = sidebarWidth
    const startX = mouseDownEvent.clientX

    function onMouseMove(mouseMoveEvent: MouseEvent) {
      const newWidth = startWidth + mouseMoveEvent.clientX - startX
      setSidebarWidth(Math.max(80, Math.min(newWidth, 320))) // Ограничиваем ширину

      document.body.style.cursor = "ew-resize"
      document.body.classList.add("select-none")
    }

    function onMouseUp() {
      document.removeEventListener("mousemove", onMouseMove)
      document.removeEventListener("mouseup", onMouseUp)

      document.body.style.cursor = ""
      document.body.classList.remove("select-none")
    }

    document.addEventListener("mousemove", onMouseMove)
    document.addEventListener("mouseup", onMouseUp)
  }

  return (
    <div className="hidden md:block md:fixed md:inset-y-0 md:z-50" style={{ width: `${sidebarWidth}px` }}>
      <div className="flex flex-col h-full border-r border-border bg-card pt-5 relative">
        {/* Область для перетаскивания */}
        <div className="absolute inset-y-0 right-0 w-2 cursor-ew-resize z-50" onMouseDown={startResize} />

        <div className="flex items-center h-16 flex-shrink-0 px-4 justify-center">
          {showText ? (
            <h1 className="text-xl font-bold truncate">Фитнес клуб</h1>
          ) : (
            <h1 className="text-xl font-bold">ФК</h1>
          )}
        </div>

        <div className="mt-5 flex-1 flex flex-col">
          <nav className="flex-1 px-2 space-y-1">
            {menuItems.map((item) => (
              <Link
                key={item.id}
                to={`/${item.id}`} // Используем to вместо href
                className={cn(
                  "group flex items-center py-3 text-sm font-medium rounded-md",
                  showText ? "px-2" : "px-0 justify-center",
                  currentPath === item.id ? "bg-primary text-primary-foreground" : "text-foreground hover:bg-muted",
                )}
                title={!showText ? item.label : ""}
              >
                <div className={showText ? "mr-3" : "mr-0"}>{item.icon}</div>
                {showText && <span className="truncate">{item.label}</span>}
              </Link>
            ))}
          </nav>
        </div>

        <div className="p-4">
          <Button className="w-full">{showText ? "Записаться" : "ЗП"}</Button>
        </div>
      </div>
    </div>
  )
}
