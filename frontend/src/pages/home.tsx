import Link from "next/link"
import { ChevronRight, Dumbbell, Users, Calendar, User } from "lucide-react"
import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardFooter, CardHeader, CardTitle } from "@/components/ui/card"
import Navbar from "@/components/navbar"
import Footer from "@/components/footer"

export default function Home() {
  return (
    <div className="flex min-h-screen flex-col">
      <Navbar />
      <main className="flex-1">
        {/* Hero Section */}
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gradient-to-r from-gray-900 to-gray-800 text-white">
          <div className="container px-4 md:px-6">
            <div className="grid gap-6 lg:grid-cols-2 lg:gap-12 items-center">
              <div className="space-y-4">
                <h1 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl lg:text-6xl">
                  Achieve Your Fitness Goals With Us
                </h1>
                <p className="max-w-[600px] text-gray-300 md:text-xl">
                  Join our fitness club and transform your body and mind with our expert trainers and state-of-the-art
                  facilities.
                </p>
                <div className="flex flex-col gap-2 min-[400px]:flex-row">
                  <Button size="lg" className="bg-primary hover:bg-primary/90">
                    Join Now
                    <ChevronRight className="ml-2 h-4 w-4" />
                  </Button>
                  <Button size="lg" variant="outline" className="border-white text-white hover:bg-white/10">
                    Learn More
                  </Button>
                </div>
              </div>
              <div className="flex justify-center">
                <img
                  src="/placeholder.svg?height=400&width=600"
                  alt="Fitness training"
                  className="rounded-lg object-cover"
                  width={600}
                  height={400}
                />
              </div>
            </div>
          </div>
        </section>

        {/* Programs Section */}
        <section className="w-full py-12 md:py-24 lg:py-32 bg-gray-50">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-5xl">Our Training Programs</h2>
                <p className="max-w-[900px] text-gray-500 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Choose from our variety of programs designed to help you reach your fitness goals.
                </p>
              </div>
            </div>
            <div className="mx-auto grid max-w-5xl gap-8 pt-12 sm:grid-cols-2 md:gap-12 lg:grid-cols-3">
              <ProgramCard
                title="Strength Training"
                description="Build muscle and increase your strength with our comprehensive strength training program."
                icon={<Dumbbell className="h-10 w-10" />}
              />
              <ProgramCard
                title="Group Fitness"
                description="Join our energetic group classes for motivation, fun, and effective workouts."
                icon={<Users className="h-10 w-10" />}
              />
              <ProgramCard
                title="Personal Training"
                description="Get personalized attention and custom workout plans with our expert trainers."
                icon={<User className="h-10 w-10" />}
              />
              <ProgramCard
                title="Cardio Fitness"
                description="Improve your cardiovascular health and endurance with our cardio-focused programs."
                icon={<Calendar className="h-10 w-10" />}
              />
              <ProgramCard
                title="Yoga & Flexibility"
                description="Enhance your flexibility, balance, and mental wellbeing with our yoga classes."
                icon={<Users className="h-10 w-10" />}
              />
              <ProgramCard
                title="Nutrition Planning"
                description="Complement your fitness routine with expert nutrition guidance and meal planning."
                icon={<Dumbbell className="h-10 w-10" />}
              />
            </div>
          </div>
        </section>

        {/* CTA Section */}
        <section className="w-full py-12 md:py-24 lg:py-32 bg-primary text-primary-foreground">
          <div className="container px-4 md:px-6">
            <div className="flex flex-col items-center justify-center space-y-4 text-center">
              <div className="space-y-2">
                <h2 className="text-3xl font-bold tracking-tighter sm:text-4xl md:text-5xl">
                  Ready to Start Your Fitness Journey?
                </h2>
                <p className="max-w-[600px] text-primary-foreground/80 md:text-xl/relaxed lg:text-base/relaxed xl:text-xl/relaxed">
                  Join our community today and transform your life with our expert guidance and support.
                </p>
              </div>
              <div className="flex flex-col gap-2 min-[400px]:flex-row">
                <Button size="lg" variant="secondary">
                  Sign Up Now
                </Button>
                <Link href="/profile">
                  <Button
                    size="lg"
                    variant="outline"
                    className="border-primary-foreground text-primary-foreground hover:bg-primary-foreground/10"
                  >
                    View My Profile
                  </Button>
                </Link>
              </div>
            </div>
          </div>
        </section>
      </main>
      <Footer />
    </div>
  )
}

function ProgramCard({ title, description, icon }) {
  return (
    <Card className="flex flex-col items-center text-center">
      <CardHeader>
        <div className="mb-2 flex h-16 w-16 items-center justify-center rounded-full bg-primary/10 text-primary">
          {icon}
        </div>
        <CardTitle className="text-xl">{title}</CardTitle>
      </CardHeader>
      <CardContent>
        <CardDescription className="text-base">{description}</CardDescription>
      </CardContent>
      <CardFooter>
        <Button variant="ghost" size="sm" className="text-primary">
          Learn more
          <ChevronRight className="ml-1 h-4 w-4" />
        </Button>
      </CardFooter>
    </Card>
  )
}

