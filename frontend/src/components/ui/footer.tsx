import {Link} from "react-router-dom"
import { Facebook, Instagram, Twitter } from "lucide-react"

export default function Footer() {
  return (
    <footer className="w-full border-t bg-background">
      <div className="container flex flex-col gap-8 px-4 py-10 md:px-6 lg:flex-row lg:gap-16">
        <div className="flex flex-col gap-2 lg:w-1/3">
          <Link to="/" className="flex items-center gap-2 font-bold text-xl">
            <Dumbbell className="h-6 w-6" />
            <span>FitClub</span>
          </Link>
          <p className="text-sm text-muted-foreground">
            Your premier fitness destination for achieving your health and wellness goals.
          </p>
        </div>
        <div className="grid flex-1 grid-cols-2 gap-8 sm:grid-cols-3">
          <div className="flex flex-col gap-2">
            <h3 className="font-medium">Navigation</h3>
            <nav className="flex flex-col gap-2">
              <Link to="/" className="text-sm hover:underline">
                Home
              </Link>
              <Link to="#programs" className="text-sm hover:underline">
                Programs
              </Link>
              <Link to="#about" className="text-sm hover:underline">
                About
              </Link>
              <Link to="#contact" className="text-sm hover:underline">
                Contact
              </Link>
            </nav>
          </div>
          <div className="flex flex-col gap-2">
            <h3 className="font-medium">Account</h3>
            <nav className="flex flex-col gap-2">
              <Link to="/profile" className="text-sm hover:underline">
                My Profile
              </Link>
              <Link to="/dashboard" className="text-sm hover:underline">
                Dashboard
              </Link>
              <Link to="/settings" className="text-sm hover:underline">
                Settings
              </Link>
            </nav>
          </div>
          <div className="flex flex-col gap-2">
            <h3 className="font-medium">Connect</h3>
            <div className="flex gap-4">
              <Link to="#" className="text-muted-foreground hover:text-foreground">
                <Facebook className="h-5 w-5" />
                <span className="sr-only">Facebook</span>
              </Link>
              <Link to="#" className="text-muted-foreground hover:text-foreground">
                <Instagram className="h-5 w-5" />
                <span className="sr-only">Instagram</span>
              </Link>
              <Link to="#" className="text-muted-foreground hover:text-foreground">
                <Twitter className="h-5 w-5" />
                <span className="sr-only">Twitter</span>
              </Link>
            </div>
          </div>
        </div>
      </div>
      <div className="border-t py-6">
        <div className="container flex flex-col items-center justify-between gap-4 px-4 md:flex-row md:px-6">
          <p className="text-center text-sm text-muted-foreground md:text-left">
            © {new Date().getFullYear()} FitClub. All rights reserved.
          </p>
          <nav className="flex gap-4">
            <Link to="#" className="text-sm text-muted-foreground hover:underline">
              Privacy Policy
            </Link>
            <Link to="#" className="text-sm text-muted-foreground hover:underline">
              Terms of Service
            </Link>
          </nav>
        </div>
      </div>
    </footer>
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

