
import { useState, useEffect } from "react"
import { Badge } from "@/components/ui/badge"
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip"
import { scheduleData } from "@/lib/schedule-data"

export function ScheduleTable() {
  const [filteredData, setFilteredData] = useState(scheduleData)

  // Получаем фильтры из localStorage (в реальном приложении это может быть состояние из контекста или Redux)
  useEffect(() => {
    // Здесь будет логика применения фильтров
    // Для демонстрации просто используем исходные данные
    setFilteredData(scheduleData)
  }, [])

  // Обновляем функцию getClassStyle, чтобы использовать стандартные цвета
  const getClassStyle = () => {
    return "bg-primary/10 text-primary hover:bg-primary/20"
  }

  // Функция для получения занятий в определенное время и день (возвращает массив)
  const getClassesForTimeAndDay = (time: string, day: number) => {
    const timeSlot = filteredData.find((slot) => slot.time === time)
    if (!timeSlot) return []

    return timeSlot.classes.filter((cls) => cls.day === day)
  }

  return (
    <div className="overflow-x-auto">
      <div className="min-w-[800px]">
        {filteredData.map((timeSlot, timeIndex) => (
          <div
            key={timeIndex}
            className={`grid grid-cols-8 ${timeIndex % 2 === 0 ? "bg-white" : "bg-muted/30"} ${
              timeIndex === filteredData.length - 1 ? "rounded-b-lg" : ""
            }`}
          >
            <div className="p-2 border-r border-t flex items-center justify-center">
              <span className="text-xs font-medium">{timeSlot.time}</span>
            </div>

            {Array.from({ length: 7 }).map((_, dayIndex) => {
              const classes = getClassesForTimeAndDay(timeSlot.time, dayIndex)

              return (
                <div
                  key={dayIndex}
                  className="p-2 border-r last:border-r-0 border-t flex flex-wrap items-center justify-center gap-1"
                >
                  {classes.length > 0
                    ? classes.map((classInfo, index) => (
                        <TooltipProvider key={index}>
                          <Tooltip>
                            <TooltipTrigger asChild>
                              <Badge className={`cursor-pointer text-xs ${getClassStyle()}`}>{classInfo.name}</Badge>
                            </TooltipTrigger>
                            <TooltipContent>
                              <div className="text-sm">
                                <p className="font-bold">{classInfo.name}</p>
                                <p>Тренер: {classInfo.trainer}</p>
                                <p>Место: {classInfo.room}</p>
                                <p>Тип: {classInfo.isIndividual ? "Индивидуальное" : "Групповое"}</p>
                              </div>
                            </TooltipContent>
                          </Tooltip>
                        </TooltipProvider>
                      ))
                    : null}
                </div>
              )
            })}
          </div>
        ))}
      </div>
    </div>
  )
}

