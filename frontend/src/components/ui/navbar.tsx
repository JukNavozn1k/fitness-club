"use client"

import { useState } from "react"
import {Link} from "react-router-dom"
import { Menu, X, User } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Sheet, SheetContent, SheetTrigger } from "@/components/ui/sheet"

export default function Navbar() {
  const [isMenuOpen, setIsMenuOpen] = useState(false)

  return (
    <header className="sticky top-0 z-50 w-full border-b bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60">
      <div className="container flex h-16 items-center justify-between px-4 md:px-6">
        <Link to="/" className="flex items-center gap-2 font-bold text-xl">
          <Dumbbell className="h-6 w-6" />
          <span>FitClub</span>
        </Link>
        <nav className="hidden md:flex gap-6">
          <Link to="/" className="text-sm font-medium hover:underline underline-offset-4">
            Home
          </Link>
          <Link to="#programs" className="text-sm font-medium hover:underline underline-offset-4">
            Programs
          </Link>
          <Link to="#about" className="text-sm font-medium hover:underline underline-offset-4">
            About
          </Link>
          <Link to="#contact" className="text-sm font-medium hover:underline underline-offset-4">
            Contact
          </Link>
        </nav>
        <div className="flex items-center gap-4">
          <Link
            to="/profile"
            className="hidden md:flex items-center gap-2 text-sm font-medium hover:underline underline-offset-4"
          >
            <User className="h-4 w-4" />
            My Profile
          </Link>
          <Button className="hidden md:inline-flex">Join Now</Button>
          <Sheet open={isMenuOpen} onOpenChange={setIsMenuOpen}>
            <SheetTrigger asChild className="md:hidden">
              <Button variant="outline" size="icon" className="rounded-full">
                {isMenuOpen ? <X className="h-5 w-5" /> : <Menu className="h-5 w-5" />}
                <span className="sr-only">Toggle menu</span>
              </Button>
            </SheetTrigger>
            <SheetContent side="right" className="w-[80%] sm:w-[350px]">
              <nav className="flex flex-col gap-4 mt-8">
                <Link to="/" className="text-lg font-medium hover:text-primary" onClick={() => setIsMenuOpen(false)}>
                  Home
                </Link>
                <Link
                  to="#programs"
                  className="text-lg font-medium hover:text-primary"
                  onClick={() => setIsMenuOpen(false)}
                >
                  Programs
                </Link>
                <Link
                  to="#about"
                  className="text-lg font-medium hover:text-primary"
                  onClick={() => setIsMenuOpen(false)}
                >
                  About
                </Link>
                <Link
                  to="#contact"
                  className="text-lg font-medium hover:text-primary"
                  onClick={() => setIsMenuOpen(false)}
                >
                  Contact
                </Link>
                <Link
                  to="/profile"
                  className="flex items-center gap-2 text-lg font-medium hover:text-primary"
                  onClick={() => setIsMenuOpen(false)}
                >
                  <User className="h-5 w-5" />
                  My Profile
                </Link>
                <Button className="mt-4" onClick={() => setIsMenuOpen(false)}>
                  Join Now
                </Button>
              </nav>
            </SheetContent>
          </Sheet>
        </div>
      </div>
    </header>
  )
}

function Dumbbell(props) {
  return (
    <svg
      {...props}
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="currentColor"
      strokeWidth="2"
      strokeLinecap="round"
      strokeLinejoin="round"
    >
      <path d="M6 7v10" />
      <path d="M18 7v10" />
      <path d="M8 7h8" />
      <path d="M8 17h8" />
      <path d="M2 9v6" />
      <path d="M22 9v6" />
      <path d="M4 9h2" />
      <path d="M4 15h2" />
      <path d="M18 9h2" />
      <path d="M18 15h2" />
    </svg>
  )
}

