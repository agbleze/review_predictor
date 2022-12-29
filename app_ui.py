from shiny import *
from test_app.api_utils import request_prediction
from constant import URL



style="color: #fff; background-color: #111213; height: 45em; background: radial-gradient(100% 514.01% at 0 0,#5b5f63 0,#404346 100%)"

style_height = "height: 26em; background-color: #babec3"

menu_style = "background-color: #63c993"


@module.ui
def get_front_interface(param = None):
    front = [
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
                                                                # ui.nav("Modelling Data", #"Describe the Modelling Data",
                                                                #     value='model_data_sidebar'),
                                                                ui.nav("Prediction", value="prediction_sidebar"),
                                                                
                                                                
                                                            ),
                                                    id="sidebar_id",
                                                    
                                
                                                ),
                                    
                                    style=style_height,
                                    ),
                    
                    ui.panel_main(ui.output_ui(id="main_output_show", ),
                                    #style=style
                                    ),
                    #style=style
                
                )
            ]
    
    return front



    # def get_homepage():
    #     pass



@module.server
def get_server_elements(input, output, session):

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
                                ui.input_action_button(id="predict", label="Prediction", style=menu_style)
                                ), 
                                ui.column(4,
                                        ui.h4("Review Prediction"), 
                                        ui.output_text(id='prediction_desc', ))
                    )
                ]
        elif selected_sidebar_dropdown == "project_desc_sidebar":
            return "This is a NLP project for predicting whether a product will be recommended based on review text"
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
        else:
            recommend_status = 'Not recommend'
            
        #return prediction
            
        return f'{recommend_status}: There is a {proba_2dp * 100}% probability that the product will be {recommend_status} based on the review'





