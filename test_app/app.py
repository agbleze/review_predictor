from shiny import *
from test_app.api_utils import request_prediction
from constant import URL



style="color: #fff; background-color: #111213; height: em; background: radial-gradient(100% 514.01% at 0 0,#5b5f63 0,#404346 100%)"

style_height = "height: 26em; background-color: #babec3"

menu_style = "background-color: #63c993"
prediction_result_style = "background-color: #bbabbc; border-radius: 3%; color: #fbeccd; font-weight: bold"

app_ui = ui.page_fluid(
                        [
                            ui.panel_title(title='Product recommendation predictor'),
                            ui.tags.br(),
                            ui.tags.h5('Predict whether product will be recommended based on review of client'),
                            ui.tags.p('Deep Learning for Natural Language Processing'),
                            ui.tags.br(),
                        
                            ui.layout_sidebar(
                                ui.panel_sidebar(
                                                ui.navset_tab(
                                                                ui.nav_menu("Menu", 
                                                                            ui.nav("Project Description", #"LET talk about Project Description",
                                                                                value="project_desc_sidebar"),
                                                                            ui.nav("Prediction", value="prediction_sidebar"),
                                                                            
                                                                            
                                                                        ),
                                                                id="sidebar_id",
                                                                
                                            
                                                            ),
                                                
                                                style=style_height,
                                                ),
                                
                                ui.panel_main(ui.output_ui(id="main_output_show", ),
                                            ),
                            )
                        ],
                        
                        style=style
                        
)


def server(input, output, session):
    @output
    @render.ui
    def main_output_show():
        selected_sidebar_dropdown = input.sidebar_id()
        if selected_sidebar_dropdown == "prediction_sidebar":
            
            
            
            return [
                    ui.row(ui.column(8,
                             ui.input_text_area(id="review", label=f"Write a product review", 
                                                width="100%", height="200px", autocomplete="on",
                                                placeholder="Write product review here", 
                                                ),
                             ui.tags.br(),
                             ui.input_action_button(id="predict", label="Predict review status", style=menu_style)
                             ), 
                             ui.column(4,
                                       ui.h4("Prediction",), 
                                       ui.tags.div(
                                                   ui.output_text(id='prediction_desc', ),  
                                                   style=prediction_result_style,
                                                   ),
                                       
                                       )
                   )
                ]
        elif selected_sidebar_dropdown == "project_desc_sidebar":
            return ui.div(ui.tags.h2('Natural Language Processing with Deep Learning'),
                          
                          ui.tags.h3('Project Description'),
                          ui.tags.br(),
                          
                          ui.tags.p("""This is a Natural Language Processing project for predicting whether 
                                    a product will be recommended based on review."""
                                    ),
                          
                          ui.tags.p("""The value this project seeks to deliver is to enable businesses analyze their product reviews and 
                                    and determine whether or not a client or customer is likely to recommend their 
                                    product or service. The tool can be used on large scale to:
                                    
                                    
                                    """
                                    ),
                          ui.tags.li('Determine after-sales and purchase intent of your customers'),
                          ui.tags.li('To augment other sales data for prediction tasks'),
                          ui.tags.li('To improve customer satisfaction by automatically identifying and resolving issues'),
                          ui.tags.li('To augment and enrich other text datasets for advance analysis'),
                          ui.tags.br(),
                          
                          ui.tags.h3('Dataset and variables used'),
                          ui.tags.br(),
                          
                          ui.tags.span("""Dataset: Product reviews provided by customers 
                                        and clients after ordering products or patronizing services.
                                        The dataset encompass variety of products and services by businesses 
                                        without focus on a single category.
                                     """
                                    ),
                          ui.tags.li("""Target variable: Recommendation status with binary values 
                                        depicting whether or not a product was recommended
                                     """),
                          ui.tags.li("""Predictor variable: Review of product which is text provided by a client or 
                                        customer who purchased the product or patronized the service
                                     
                                     """),
                          
                          ui.tags.h4('Method of analysis'),
                          ui.tags.p("""The reviews were preprocessed, vectorized and an embedding matrix developed. A neural network 
                                        architecture was developed and feed with processed data for training and validation of model
                                    """),
                          
                          ui.tags.h4('Programming tools used'),
                          ui.tags.li('Pandas and Numpy for data cleaning and other preprocessing'),
                          ui.tags.li('PyTorch as framework for developing the neural network architecture'),
                          ui.tags.li('Flask as framework for developing Deep learning API to serve the model'),
                          ui.tags.li('Python Shiny for developing this User Interface'),
                          ui.tags.li('Python as the programming langauge'),
                          
                          ui.tags.h4("Result"),
                          ui.tags.p("""1. A Deep learning API 
                                        that accepts a product review and predict whether 
                                        client is likely to recommend the product 
                                    """),
                          ui.tags.p("""2. A web application backed by deep learning that provides an 
                                        interface for writing reviews and making predictions
                                    """),
               
                          )
        else:
            return "Describe model data"
    
    @output
    @render.text    
    @reactive.event(input.predict, ignore_none=True)    
    def prediction_desc():
        review = input.review()
        prediction = request_prediction(URL=URL, review_data=review)
        
        category = prediction['category']
        probability = prediction['probability']
        proba_2dp = round(probability, 2)
        
        if category == True:
            recommend_status = 'Recommend'
            message = '% probability that the product will be recommended based on review'
        else:
            recommend_status = 'Not recommend'
            message = '% probability that the product will not be recommended based on review'
            
        return f'{recommend_status}:   There is a {proba_2dp * 100} {message}'

app = App(app_ui, server)





