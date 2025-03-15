import LoginForm from "./pages/login"

function App() {
  return (
    <>
     <main className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-br from-blue-50 to-blue-100 p-4">
      <div className="w-full max-w-md">
        <LoginForm />
      </div>
    </main>
    </>
  )
}

export default App
