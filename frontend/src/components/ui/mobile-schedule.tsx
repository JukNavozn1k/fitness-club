import { useState, useEffect } from "react"
import { Badge } from "@/components/ui/badge"
import { Card, CardContent, CardHeader } from "@/components/ui/card"
import { Tabs, TabsContent, TabsList, TabsTrigger } from "@/components/ui/tabs"
import { scheduleData } from "@/lib/schedule-data"
import { useFilters } from "@/components/ui/schedule-filters"

export function MobileSchedule() {
  const days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
  const [filteredData, setFilteredData] = useState(scheduleData)

  const { selectedTrainers, selectedClassTypes, selectedSessionType, showOnlyMyClasses } = useFilters()

  // Получаем текущий день недели (0 - воскресенье, 1 - понедельник, и т.д.)
  const today = new Date().getDay()
  // Преобразуем в наш формат (0 - понедельник, 6 - воскресенье)
  const currentDay = today === 0 ? 6 : today - 1

  const [selectedDay, setSelectedDay] = useState(currentDay.toString())

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

  // Функция для получения классов для определенного дня
  const getClassesForDay = (dayIndex: number) => {
    const dayClasses = []

    for (const timeSlot of filteredData) {
      const classesForTime = timeSlot.classes.filter((cls) => cls.day === dayIndex)

      if (classesForTime.length > 0) {
        dayClasses.push({
          time: timeSlot.time,
          classes: classesForTime,
        })
      }
    }

    return dayClasses
  }

  return (
    <div className="space-y-4">
      <Tabs defaultValue={selectedDay} onValueChange={setSelectedDay}>
        <TabsList className="w-full grid grid-cols-7 h-auto">
          {days.map((day, index) => (
            <TabsTrigger key={index} value={index.toString()} className="text-xs py-2 px-1 sm:text-sm sm:px-2">
              {day.substring(0, 3)}
            </TabsTrigger>
          ))}
        </TabsList>

        {days.map((day, index) => (
          <TabsContent key={index} value={index.toString()}>
            <Card>
              <CardHeader className="py-3 px-4 border-b">
                <h3 className="font-medium text-center">{day}</h3>
              </CardHeader>
              <CardContent className="p-0">
                {getClassesForDay(index).length > 0 ? (
                  <div className="divide-y">
                    {getClassesForDay(index).map((timeSlot, timeIndex) => (
                      <div key={timeIndex} className="p-4">
                        <div className="font-medium text-sm mb-2">{timeSlot.time}</div>
                        <div className="space-y-3">
                          {timeSlot.classes.map((cls, clsIndex) => (
                            <div key={clsIndex} className="flex items-start gap-3 bg-muted/30 p-3 rounded-md">
                              <Badge className={`mt-0.5 ${cls.isMyClass ? "bg-primary text-primary-foreground" : ""}`}>
                                {cls.name}
                              </Badge>
                              <div>
                                <div className="font-medium">{cls.name}</div>
                                <div className="text-sm text-muted-foreground">Тренер: {cls.trainer}</div>
                                <div className="text-sm text-muted-foreground">Зал: {cls.room}</div>
                                <div className="text-sm text-muted-foreground">
                                  Тип: {cls.isIndividual ? "Индивидуальное" : "Групповое"}
                                </div>
                                {cls.isMyClass && (
                                  <div className="text-sm font-semibold text-primary mt-1">Моё занятие</div>
                                )}
                              </div>
                            </div>
                          ))}
                        </div>
                      </div>
                    ))}
                  </div>
                ) : (
                  <div className="p-8 text-center text-muted-foreground">Нет занятий в этот день</div>
                )}
              </CardContent>
            </Card>
          </TabsContent>
        ))}
      </Tabs>
    </div>
  )
}

