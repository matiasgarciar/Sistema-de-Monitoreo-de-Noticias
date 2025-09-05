import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import (
	SerperDevTool,
	EXASearchTool,
	SerplyNewsSearchTool,
	ScrapeWebsiteTool
)



@CrewBase
class BusinessNewsIntelligenceMonitorCrew:
    """BusinessNewsIntelligenceMonitor crew"""

    
    @agent
    def business_news_research_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["business_news_research_specialist"],
            tools=[SerperDevTool(), EXASearchTool(), SerplyNewsSearchTool()],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def content_extraction_specialist(self) -> Agent:
        
        return Agent(
            config=self.agents_config["content_extraction_specialist"],
            tools=[ScrapeWebsiteTool()],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def executive_intelligence_analyst(self) -> Agent:
        
        return Agent(
            config=self.agents_config["executive_intelligence_analyst"],
            tools=[],
            reasoning=False,
            inject_date=True,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    

    
    @task
    def comprehensive_news_search(self) -> Task:
        return Task(
            config=self.tasks_config["comprehensive_news_search"],
        )
    
    @task
    def full_content_extraction(self) -> Task:
        return Task(
            config=self.tasks_config["full_content_extraction"],
        )
    
    @task
    def executive_intelligence_report(self) -> Task:
        return Task(
            config=self.tasks_config["executive_intelligence_report"],
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the BusinessNewsIntelligenceMonitor crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
