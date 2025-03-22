"use client"

import { Link, useLocation } from "react-router-dom"
import { Home, Calendar, User, CreditCard, Dumbbell } from "lucide-react"
import { cn } from "@/lib/utils"

export default function MobileNavbar() {
  const location = useLocation()
  const currentPath = location.pathname.substring(1) || "home"

  const menuItems = [
    { id: "home", label: "Главная", icon: <Home className="h-5 w-5" /> },
    { id: "schedule", label: "Расписание", icon: <Calendar className="h-5 w-5" /> },
    { id: "profile", label: "Профиль", icon: <User className="h-5 w-5" /> },
    { id: "subscriptions", label: "Абонементы", icon: <CreditCard className="h-5 w-5" /> },
    { id: "services", label: "Услуги", icon: <Dumbbell className="h-5 w-5" /> },
  ]

  return (
    <div className="md:hidden fixed bottom-0 left-0 right-0 bg-background border-t border-border z-50">
      <div className="grid grid-cols-5">
        {menuItems.map((item) => (
          <Link
            key={item.id}
            to={`/${item.id}`}
            className={cn(
              "flex flex-col items-center justify-center py-3",
              currentPath === item.id ? "text-primary" : "text-muted-foreground",
            )}
          >
            <div className="mb-1">{item.icon}</div>
            <span className="text-xs">{item.label}</span>
          </Link>
        ))}
      </div>
    </div>
  )
}
