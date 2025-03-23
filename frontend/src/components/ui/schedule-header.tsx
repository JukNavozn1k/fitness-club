export function ScheduleHeader() {
    const days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
  
    return (
      <div className="grid grid-cols-8 bg-muted rounded-t-lg">
        <div className="p-2 font-medium text-center border-r text-sm">Время</div>
        {days.map((day, index) => (
          <div key={index} className="p-2 font-medium text-center border-r last:border-r-0 text-sm">
            {day}
          </div>
        ))}
      </div>
    )
  }
  
  