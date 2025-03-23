"use client"

import { useState } from "react"
import { ChevronLeft, ChevronRight } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select"

export function WeekSelector() {
  const [currentWeek, setCurrentWeek] = useState("current")

  // Получаем текущую дату
  const today = new Date()
  const currentDay = today.getDate()
  const currentMonth = today.getMonth()
  const currentYear = today.getFullYear()

  // Функция для форматирования даты
  const formatDate = (date: Date) => {
    return date.toLocaleDateString("ru-RU", {
      day: "numeric",
      month: "long",
    })
  }

  // Получаем начало и конец текущей недели
  const getWeekDates = () => {
    const now = new Date(currentYear, currentMonth, currentDay)
    const dayOfWeek = now.getDay() || 7 // Преобразуем 0 (воскресенье) в 7

    // Начало недели (понедельник)
    const startOfWeek = new Date(now)
    startOfWeek.setDate(now.getDate() - dayOfWeek + 1)

    // Конец недели (воскресенье)
    const endOfWeek = new Date(now)
    endOfWeek.setDate(now.getDate() + (7 - dayOfWeek))

    return {
      start: formatDate(startOfWeek),
      end: formatDate(endOfWeek),
    }
  }

  const weekDates = getWeekDates()

  return (
    <div className="flex flex-col sm:flex-row items-center justify-between gap-4">
      <div className="flex items-center gap-2">
        <Button variant="outline" size="icon">
          <ChevronLeft className="h-4 w-4" />
        </Button>
        <div className="text-lg font-medium">
          {weekDates.start} - {weekDates.end}
        </div>
        <Button variant="outline" size="icon">
          <ChevronRight className="h-4 w-4" />
        </Button>
      </div>

      <div className="flex items-center gap-4">
        <Button variant="outline" onClick={() => setCurrentWeek("current")}>
          Сегодня
        </Button>

        <Select value={currentWeek} onValueChange={setCurrentWeek}>
          <SelectTrigger className="w-[180px]">
            <SelectValue placeholder="Выберите неделю" />
          </SelectTrigger>
          <SelectContent>
            <SelectItem value="current">Текущая неделя</SelectItem>
            <SelectItem value="next">Следующая неделя</SelectItem>
            <SelectItem value="after-next">Через неделю</SelectItem>
          </SelectContent>
        </Select>
      </div>
    </div>
  )
}

