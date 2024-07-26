def refereceData(ProjectTitle,
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
    data = f"""
           You are an expert in creating bidding and proposal reports in the construction industry. Create a Bidding and Proposal report based on the following inputs:

                Project Title: {ProjectTitle}

                Client Name: {CompanyName}

                Project Location: {ProjectLocation}

                ---

                ### 1. Executive Summary

                {CompanyName} intends to develop {ProjectTitle} at {ProjectLocation}. The project will consist of {NumberOfApartments} units/apartments with amenities including {Amenities}. This proposal outlines the project scope, timeline, cost estimates, and our qualifications as a construction contractor.

                ### 2. Project Scope

                **2.1. Site Preparation**

                - Clearing and grading the site
                - Excavation for foundations and utilities
                - Erosion control measures

                **2.2. Construction**

                - Foundation work (footings, slab)
                - Framing (wood/steel)
                - Roofing
                - Exterior finishes (brick, siding)
                - Interior finishes (drywall, flooring, painting)
                - Installation of windows and doors

                **2.3. Mechanical, Electrical, and Plumbing (MEP)**

                - HVAC systems
                - Electrical wiring and fixtures
                - Plumbing systems (water supply, drainage)
                - Fire protection systems

                **2.4. Amenities**

                - Construction of {Amenities}

                **2.5. Landscaping**

                - Planting trees and shrubs
                - Lawn installation
                - Irrigation system

                ### 3. Project Timeline

                The project is scheduled to start on {StartDate} and is expected to be completed by {EndDate}, and the design preference will be {DesignPreferences}.

                ### 4. Cost Estimates

                | Item                            | Cost (USD)       |
                |---------------------------------|------------------|
                | Site Preparation                | {{SitePrepCost}}   |
                | Foundation Work                 | {{FoundationCost}} |
                | Framing                         | {{FramingCost}}    |
                | Roofing and Exterior Finishes   | {{RoofingCost}}    |
                | Interior Finishes               | {{InteriorCost}}   |
                | MEP Installation                | {{MEPCost}}        |
                | Amenities Construction          | {{AmenitiesCost}}  |
                | Landscaping                     | {{LandscapingCost}}|
                | **Total Estimated Cost**        | **{EstimatedBudget}** |

                ### 5. Contractor Qualifications

                **Company Name:** {CompanyName}

                **Experience:**

                - Over 20 years of experience in residential and commercial construction.
                - Successfully completed 100+ residential projects, including luxury apartment complexes.
                - Strong reputation for quality workmanship and timely project completion.

                **Key Personnel:**

                - **{ProjectManagerName}, Project Manager:** 25 years of experience in construction management.

                ### 6. Terms and Conditions

                - **Payment Schedule:** Payments will be made in installments based on the completion of each project phase.
                - **Change Orders:** Any changes to the project scope will be documented and may incur additional costs.
                - **Warranty:** A one-year warranty will be provided for all construction work.
                - **Insurance:** XYZ Construction Inc. is fully insured and will provide proof of insurance upon request.

                ### 7. Contact Information

                **{CompanyName}**

                - **Address:** {CompanyAddress}
                - **Phone:** {CompanyPhone}
                - **Email:** {CompanyEmail}

                ---

                **Prepared by:**

                **{ProjectManagerName}**

                Project Manager, {CompanyName}

                        """
    
    return data


def taskPrompt():
    prompt = """
                Create a full Bidding and proposal report for the USER.

            """
    
    return prompt