import { ScheduleHeader } from "@/components/ui/schedule-header"
import { ScheduleTable } from "@/components/ui/schedule-table"
import { WeekSelector } from "@/components/ui/week-selector"
import { ScheduleFilters, FiltersProvider } from "@/components/ui/schedule-filters"
import { MobileSchedule } from "@/components/ui/mobile-schedule"

export default function Schedule() {
  return (
    <FiltersProvider>
      <div className="container mx-auto py-8 px-4">
        <h1 className="text-3xl font-bold mb-6 text-center">Фитнес Клуб "Энергия"</h1>
        <p className="text-center text-muted-foreground mb-8">Расписание занятий на неделю</p>

        <div className="mb-8">
          <WeekSelector />
        </div>

        <div className="mb-8">
          <ScheduleFilters />
        </div>

        {/* Десктопная версия - скрыта на мобильных */}
        <div className="hidden md:block rounded-lg border bg-card shadow">
          <ScheduleHeader />
          <ScheduleTable />
        </div>

        {/* Мобильная версия - видна только на мобильных */}
        <div className="md:hidden">
          <MobileSchedule />
        </div>
      </div>
    </FiltersProvider>
  )
}

