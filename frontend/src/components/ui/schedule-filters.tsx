import type React from "react"

import { useState } from "react"
import { Check, ChevronsUpDown, X } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Command, CommandEmpty, CommandGroup, CommandInput, CommandItem, CommandList } from "@/components/ui/command"
import { Popover, PopoverContent, PopoverTrigger } from "@/components/ui/popover"
import { Badge } from "@/components/ui/badge"
import { Checkbox } from "@/components/ui/checkbox"
import { Label } from "@/components/ui/label"
import { cn } from "@/lib/utils"
import { trainers, classTypes } from "@/lib/schedule-data"

// Создаем контекст для фильтров
import { createContext, useContext } from "react"

type FiltersContextType = {
  selectedTrainers: string[]
  selectedClassTypes: string[]
  selectedSessionType: string | null
  showOnlyMyClasses: boolean
  setSelectedTrainers: (trainers: string[]) => void
  setSelectedClassTypes: (types: string[]) => void
  setSelectedSessionType: (type: string | null) => void
  setShowOnlyMyClasses: (show: boolean) => void
}

export const FiltersContext = createContext<FiltersContextType>({
  selectedTrainers: [],
  selectedClassTypes: [],
  selectedSessionType: null,
  showOnlyMyClasses: false,
  setSelectedTrainers: () => {},
  setSelectedClassTypes: () => {},
  setSelectedSessionType: () => {},
  setShowOnlyMyClasses: () => {},
})

export const useFilters = () => useContext(FiltersContext)

export function FiltersProvider({ children }: { children: React.ReactNode }) {
  const [selectedTrainers, setSelectedTrainers] = useState<string[]>([])
  const [selectedClassTypes, setSelectedClassTypes] = useState<string[]>([])
  const [selectedSessionType, setSelectedSessionType] = useState<string | null>(null)
  const [showOnlyMyClasses, setShowOnlyMyClasses] = useState(false)

  return (
    <FiltersContext.Provider
      value={{
        selectedTrainers,
        selectedClassTypes,
        selectedSessionType,
        showOnlyMyClasses,
        setSelectedTrainers,
        setSelectedClassTypes,
        setSelectedSessionType,
        setShowOnlyMyClasses,
      }}
    >
      {children}
    </FiltersContext.Provider>
  )
}

export function ScheduleFilters() {
  const [openTrainer, setOpenTrainer] = useState(false)
  const [openClassType, setOpenClassType] = useState(false)
  const [openSessionType, setOpenSessionType] = useState(false)

  const {
    selectedTrainers,
    selectedClassTypes,
    selectedSessionType,
    showOnlyMyClasses,
    setSelectedTrainers,
    setSelectedClassTypes,
    setSelectedSessionType,
    setShowOnlyMyClasses,
  } = useFilters()

  // Получаем уникальный список тренеров
  const trainersList = trainers

  // Получаем уникальный список типов занятий
  const classTypesList = classTypes

  // Типы сессий
  const sessionTypes = ["Групповое", "Индивидуальное"]

  // Функция для очистки всех фильтров
  const clearAllFilters = () => {
    setSelectedTrainers([])
    setSelectedClassTypes([])
    setSelectedSessionType(null)
    setShowOnlyMyClasses(false)
  }

  // Функция для удаления одного фильтра
  const removeFilter = (type: string, value: string) => {
    if (type === "trainer") {
      setSelectedTrainers(selectedTrainers.filter((t) => t !== value))
    } else if (type === "class") {
      setSelectedClassTypes(selectedClassTypes.filter((c) => c !== value))
    } else if (type === "session") {
      setSelectedSessionType(null)
    }
  }

  // Проверяем, есть ли активные фильтры
  const hasActiveFilters =
    selectedTrainers.length > 0 || selectedClassTypes.length > 0 || selectedSessionType !== null || showOnlyMyClasses

  return (
    <div className="space-y-4">
      <div className="flex flex-wrap gap-2">
        <Popover open={openClassType} onOpenChange={setOpenClassType}>
          <PopoverTrigger asChild>
            <Button variant="outline" role="combobox" aria-expanded={openClassType} className="justify-between">
              <span>Тип тренировки</span>
              <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50" />
            </Button>
          </PopoverTrigger>
          <PopoverContent className="w-[200px] p-0">
            <Command>
              <CommandInput placeholder="Поиск типа..." />
              <CommandList>
                <CommandEmpty>Не найдено</CommandEmpty>
                <CommandGroup>
                  {classTypesList.map((classType) => (
                    <CommandItem
                      key={classType}
                      value={classType}
                      onSelect={() => {
                        setSelectedClassTypes(
                          selectedClassTypes.includes(classType)
                            ? selectedClassTypes.filter((t) => t !== classType)
                            : [...selectedClassTypes, classType],
                        )
                      }}
                    >
                      <Check
                        className={cn(
                          "mr-2 h-4 w-4",
                          selectedClassTypes.includes(classType) ? "opacity-100" : "opacity-0",
                        )}
                      />
                      {classType}
                    </CommandItem>
                  ))}
                </CommandGroup>
              </CommandList>
            </Command>
          </PopoverContent>
        </Popover>

        <Popover open={openTrainer} onOpenChange={setOpenTrainer}>
          <PopoverTrigger asChild>
            <Button variant="outline" role="combobox" aria-expanded={openTrainer} className="justify-between">
              <span>Тренер</span>
              <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50" />
            </Button>
          </PopoverTrigger>
          <PopoverContent className="w-[200px] p-0">
            <Command>
              <CommandInput placeholder="Поиск тренера..." />
              <CommandList>
                <CommandEmpty>Не найдено</CommandEmpty>
                <CommandGroup>
                  {trainersList.map((trainer) => (
                    <CommandItem
                      key={trainer}
                      value={trainer}
                      onSelect={() => {
                        setSelectedTrainers(
                          selectedTrainers.includes(trainer)
                            ? selectedTrainers.filter((t) => t !== trainer)
                            : [...selectedTrainers, trainer],
                        )
                      }}
                    >
                      <Check
                        className={cn("mr-2 h-4 w-4", selectedTrainers.includes(trainer) ? "opacity-100" : "opacity-0")}
                      />
                      {trainer}
                    </CommandItem>
                  ))}
                </CommandGroup>
              </CommandList>
            </Command>
          </PopoverContent>
        </Popover>

        <Popover open={openSessionType} onOpenChange={setOpenSessionType}>
          <PopoverTrigger asChild>
            <Button variant="outline" role="combobox" aria-expanded={openSessionType} className="justify-between">
              <span>Тип занятия</span>
              <ChevronsUpDown className="ml-2 h-4 w-4 shrink-0 opacity-50" />
            </Button>
          </PopoverTrigger>
          <PopoverContent className="w-[200px] p-0">
            <Command>
              <CommandList>
                <CommandEmpty>Не найдено</CommandEmpty>
                <CommandGroup>
                  {sessionTypes.map((type) => (
                    <CommandItem
                      key={type}
                      value={type}
                      onSelect={() => {
                        setSelectedSessionType(selectedSessionType === type ? null : type)
                      }}
                    >
                      <Check
                        className={cn("mr-2 h-4 w-4", selectedSessionType === type ? "opacity-100" : "opacity-0")}
                      />
                      {type}
                    </CommandItem>
                  ))}
                </CommandGroup>
              </CommandList>
            </Command>
          </PopoverContent>
        </Popover>

        <div className="flex items-center space-x-2">
          <Checkbox
            id="my-classes"
            checked={showOnlyMyClasses}
            onCheckedChange={(checked) => setShowOnlyMyClasses(checked as boolean)}
          />
          <Label
            htmlFor="my-classes"
            className="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70"
          >
            Только мои занятия
          </Label>
        </div>

        {hasActiveFilters && (
          <Button variant="ghost" size="sm" onClick={clearAllFilters} className="h-10">
            Сбросить все
          </Button>
        )}
      </div>

      {/* Отображение активных фильтров */}
      {hasActiveFilters && (
        <div className="flex flex-wrap gap-2 pt-2">
          {selectedClassTypes.map((classType) => (
            <Badge key={`class-${classType}`} variant="secondary" className="flex items-center gap-1">
              {classType}
              <X className="h-3 w-3 cursor-pointer" onClick={() => removeFilter("class", classType)} />
            </Badge>
          ))}

          {selectedTrainers.map((trainer) => (
            <Badge key={`trainer-${trainer}`} variant="secondary" className="flex items-center gap-1">
              {trainer}
              <X className="h-3 w-3 cursor-pointer" onClick={() => removeFilter("trainer", trainer)} />
            </Badge>
          ))}

          {selectedSessionType && (
            <Badge variant="secondary" className="flex items-center gap-1">
              {selectedSessionType}
              <X className="h-3 w-3 cursor-pointer" onClick={() => removeFilter("session", selectedSessionType)} />
            </Badge>
          )}

          {showOnlyMyClasses && (
            <Badge variant="secondary" className="flex items-center gap-1">
              Только мои занятия
              <X className="h-3 w-3 cursor-pointer" onClick={() => setShowOnlyMyClasses(false)} />
            </Badge>
          )}
        </div>
      )}
    </div>
  )
}

