from django.test import TestCase

from matcher.models import Matching
from api.models import Startup, Investor

startup = Startup.objects.first()
# investitori filtrati su industria,type of busines stage e type of investement
# investors = list(Investor.objects.filter(industry = startup.industry, type_of_business= startup.type_of_business, stage = startup.stage, type_of_investment=startup.type_of_investment))
investors = list(Investor.objects.all())
matches =[]

def matching():
    for investor in investors:
        # filtri su: 'industry', 'type_of_business', 'stage', 'type_of_investment'
        startup_filt = list(Startup.objects.filter(industry = investor.industry, type_of_business= investor.type_of_business, stage = investor.stage, type_of_investment=investor.type_of_investment))
        if len(startup_filt) == 0:
            continue
        for startup in startup_filt:
            # filtro sdg
            sdg_stp = set(startup.sdg.values())
            sdg_inv = set(investor.sdg.values())
            common_sdg = sdg_stp.intersection(sdg_inv)
            if len(common_sdg) == 0:
                continue
            # filtro impact_value
            print ( 'startup: '+ startup.name + ' , investor:  ' + investor.company_name)
            if investor.impact_value <= startup.impact_value +1 and investor.impact_value >= startup.impact_value -1:
                lan_inv = set(investor.languages)
                lan_stp = set(startup.team_languages)
                common_languages = lan_inv.intersection(lan_stp)
                # filtro lingue
                print('qui entro')
                if len(common_languages) == 0:
                    continue
                else:
                    print('qui entro')
                    values_stp = set(startup.team_values)
                    values_inv = set(investor.team_values)
                    common_values = values_stp.intersection(values_inv)
                    # filtro team_values
                    if len(common_values) == 0:
                        continue
                    score = 50
                    if len(common_values)>=3:
                        score+= 10
                    score = 50
                    if startup.financial_tables:
                        score +=5
                    motives_stp = set(startup.team_motives)
                    motive_inv = set(investor.team_motives)
                    common_motives = motives_stp.intersection(motive_inv)
                    if len(common_motives)>0:
                        score += 10
                    expertice_stp = set(startup.investor_expertise)
                    expertice_inv = set(investor.investor_expertise)
                    common_expertice = expertice_stp.intersection(expertice_inv)
                    if len(common_expertice)>0:
                        score += 5
                        if len(common_expertice)>3:
                            score +=5
                    matches.append((startup, investor, score))


# mancano i check su expectations, instrument, use of founds
                    
                    