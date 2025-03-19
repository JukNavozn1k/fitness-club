"use client"

import { useState } from "react"
import { Link, useLocation } from "react-router-dom" // Используем React Router Link и useLocation
import { Home, Dumbbell, Users, Phone } from "lucide-react"
import { cn } from "@/lib/utils"

export default function MobileNavbar() {
  const location = useLocation()
  const currentPath = location.pathname.substring(1) || "home"

  const menuItems = [
    { id: "home", label: "Главная", icon: <Home className="h-5 w-5" /> },
    { id: "services", label: "Услуги", icon: <Dumbbell className="h-5 w-5" /> },
    { id: "trainers", label: "Тренеры", icon: <Users className="h-5 w-5" /> },
    { id: "contact", label: "Контакты", icon: <Phone className="h-5 w-5" /> },
  ]

  return (
    <div className="md:hidden fixed bottom-0 left-0 right-0 bg-background border-t border-border z-50">
      <div className="grid grid-cols-4">
        {menuItems.map((item) => (
          <Link
            key={item.id}
            to={`/${item.id}`} // Используем to вместо href
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
