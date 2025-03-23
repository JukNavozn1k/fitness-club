"use client"

import { useState, useEffect } from "react"
import { Badge } from "@/components/ui/badge"
import { Tooltip, TooltipContent, TooltipProvider, TooltipTrigger } from "@/components/ui/tooltip"
import { scheduleData } from "@/lib/schedule-data"
import { useFilters } from "@/components/ui/schedule-filters"

export function ScheduleTable() {
  const [filteredData, setFilteredData] = useState(scheduleData)
  const { selectedTrainers, selectedClassTypes, selectedSessionType, showOnlyMyClasses } = useFilters()

  // Применяем фильтры при их изменении
  useEffect(() => {
    let newData = [...scheduleData]

    // Создаем новый массив с отфильтрованными классами для каждого временного слота
    newData = newData.map((timeSlot) => {
      let filteredClasses = [...timeSlot.classes]

      // Фильтр по типу тренировки
      if (selectedClassTypes.length > 0) {
        filteredClasses = filteredClasses.filter((cls) => selectedClassTypes.includes(cls.name))
      }

      // Фильтр по тренеру
      if (selectedTrainers.length > 0) {
        filteredClasses = filteredClasses.filter((cls) => selectedTrainers.includes(cls.trainer))
      }

      // Фильтр по типу занятия (групповое/индивидуальное)
      if (selectedSessionType) {
        const isIndividual = selectedSessionType === "Индивидуальное"
        filteredClasses = filteredClasses.filter((cls) => cls.isIndividual === isIndividual)
      }

      // Фильтр "только мои занятия"
      if (showOnlyMyClasses) {
        filteredClasses = filteredClasses.filter((cls) => cls.isMyClass)
      }

      return {
        ...timeSlot,
        classes: filteredClasses,
      }
    })

    // Фильтруем временные слоты, в которых не осталось занятий
    newData = newData.filter((timeSlot) => timeSlot.classes.length > 0)

    setFilteredData(newData)
  }, [selectedTrainers, selectedClassTypes, selectedSessionType, showOnlyMyClasses])

  // Обновляем функцию getClassStyle, чтобы использовать стандартные цвета
  // и выделять "мои занятия"
  const getClassStyle = (isMyClass: boolean) => {
    return isMyClass
      ? "bg-primary text-primary-foreground hover:bg-primary/90"
      : "bg-primary/10 text-primary hover:bg-primary/20"
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
                              <Badge className={`cursor-pointer text-xs ${getClassStyle(classInfo.isMyClass)}`}>
                                {classInfo.name}
                              </Badge>
                            </TooltipTrigger>
                            <TooltipContent>
                              <div className="text-sm">
                                <p className="font-bold">{classInfo.name}</p>
                                <p>Тренер: {classInfo.trainer}</p>
                                <p>Место: {classInfo.room}</p>
                                <p>Тип: {classInfo.isIndividual ? "Индивидуальное" : "Групповое"}</p>
                                {classInfo.isMyClass && <p className="font-semibold text-primary">Моё занятие</p>}
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

