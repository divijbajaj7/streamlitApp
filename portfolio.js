import React from "react";
import { Card, CardContent } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Mail, Github, Linkedin } from "lucide-react";

export default function PortfolioSite() {
  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <header className="text-center mb-12">
        <h1 className="text-4xl font-bold mb-2">Hi, I'm Divij Bajaj</h1>
        <p className="text-gray-600 text-lg">Data & Applied Scientist | AI Enthusiast | Educator</p>
        <div className="flex justify-center space-x-4 mt-4">
          <a href="mailto:divij@example.com"><Mail /></a>
          <a href="https://github.com/yourgithub" target="_blank" rel="noreferrer"><Github /></a>
          <a href="https://linkedin.com/in/yourlinkedin" target="_blank" rel="noreferrer"><Linkedin /></a>
        </div>
      </header>

      <section className="mb-12">
        <h2 className="text-2xl font-semibold mb-4">About Me</h2>
        <p className="text-gray-700 max-w-2xl mx-auto">
          I work at the intersection of data, AI, and real-world problem solving. With experience in building intelligent systems, delivering workshops, and mentoring students, I aim to make technology more useful and accessible for everyone.
        </p>
      </section>

      <section className="mb-12">
        <h2 className="text-2xl font-semibold mb-4">Projects</h2>
        <div className="grid md:grid-cols-2 gap-6">
          <Card>
            <CardContent className="p-4">
              <h3 className="text-xl font-bold">Log Intelligence</h3>
              <p className="text-gray-600 text-sm mb-2">Embedding Drift-Based Anomaly Detection for Incident Response</p>
              <Button variant="outline" asChild>
                <a href="https://github.com/yourgithub/log-intelligence" target="_blank">View Project</a>
              </Button>
            </CardContent>
          </Card>

          <Card>
            <CardContent className="p-4">
              <h3 className="text-xl font-bold">AI Workshop Series</h3>
              <p className="text-gray-600 text-sm mb-2">Delivered hands-on sessions on GenAI, Prompt Engineering, Market Research, and more.</p>
              <Button variant="outline" asChild>
                <a href="https://example.com/workshops" target="_blank">View Details</a>
              </Button>
            </CardContent>
          </Card>
        </div>
      </section>

      <section>
        <h2 className="text-2xl font-semibold mb-4">Contact</h2>
        <p className="text-gray-700 max-w-xl mx-auto">
          I'm open to collaboration, speaking engagements, and freelance consulting. Drop me a message and let's connect.
        </p>
        <div className="flex justify-center mt-4">
          <Button>
            <a href="mailto:divij@example.com">Get In Touch</a>
          </Button>
        </div>
      </section>
    </div>
  );
}
