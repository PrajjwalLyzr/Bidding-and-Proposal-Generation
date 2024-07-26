from lyzr_automata.ai_models.openai import OpenAIModel
from lyzr_automata import Agent, Task
from lyzr_automata.tasks.task_literals import InputType, OutputType
from lyzr_automata.pipelines.linear_sync_pipeline  import  LinearSyncPipeline
from lyzr_automata import Logger
from prompts.prompts import refereceData
from dotenv import load_dotenv; load_dotenv()



def bidding_proposal_generation(ApiKey,
                                ProjectTitle,
                                ProjectLocation,
                                StartDate,
                                EndDate,
                                Amenities,
                                NumberOfApartments,
                                DesignPreferences,
                                EstimatedBudget,
                                CompanyName,
                                ProjectManagerName,
                                CompanyAddress, 
                                CompanyPhone, 
                                CompanyEmail):
    open_ai_model_text = OpenAIModel(
        api_key= ApiKey,
        parameters={
            "model": "gpt-4o",
            "temperature": 0.5,
            "max_tokens": 1500,
        },
    )

    bidding_drafter = Agent(
        prompt_persona=refereceData(ProjectTitle,
                                ProjectLocation,
                                StartDate,
                                EndDate,
                                Amenities,
                                NumberOfApartments,
                                DesignPreferences,
                                EstimatedBudget,
                                CompanyName,
                                ProjectManagerName,
                                CompanyAddress, 
                                CompanyPhone, 
                                CompanyEmail),
    
        role="Bidding Drafter", 
    )

    BiddingProposal_generator =  Task(
        name="Bidding Proposal Generator",
        agent=bidding_drafter,
        output_type=OutputType.TEXT,
        input_type=InputType.TEXT,
        model=open_ai_model_text,
        instructions="Create a full Bidding and proposal report for the USER.",
        enhance_prompt=False
    )


    logger = Logger()
    

    main_output = LinearSyncPipeline(
        logger=logger,
        name="Bidding and Proposal Generator ",
        completion_message="App Generated all things!",
        tasks=[
            BiddingProposal_generator,
        ],
    ).run()

    return main_output