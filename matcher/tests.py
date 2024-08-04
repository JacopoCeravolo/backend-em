
# for the testing of the alghorithm:
# python3 manage.py shell
# copy all the code of this file and paste it into the shell
# actually using this file for testing: initialize_startups.py, initialize_investors .py
from matcher.models import Matching
from api.models import Startup, Investor

# investitori filtrati su industria,type of busines stage e type of investement
investors = list(Investor.objects.all())
matches =[]

def matching():
    for investor in investors:
        
        # filtri su: 'industry', 'type_of_business', 'type_of_investment'
        startup_filt = list(Startup.objects.filter(industry = investor.industry, type_of_business= investor.type_of_business, type_of_investment=investor.type_of_investment))
        print(startup_filt)
        if len(startup_filt) == 0:
            print(f'(0) - Initial filters not passed:\n. Investor: {investor}\n. Startups: {startup_filt}\n')
            continue
        for startup in startup_filt:
            sdg_stp = set(startup.sdg.values())
            sdg_inv = set(investor.sdg.values())
            common_sdg = sdg_stp.intersection(sdg_inv)
            # filtro sdg
            if len(common_sdg) == 0:
                print(f'(1) - sdg filter not passed:\n. Investor: {investor}, {sdg_inv}\n. Startup: {startup}, {sdg_stp}\n')
                continue
            # filtro impact_value
            if not investor.impact_value <= startup.impact_value +1 or not investor.impact_value >= startup.impact_value -1:
                print(f'(2) - impact value filter not passed:\n. Investor: {investor}, {investor.impact_value}\n. Startup: {startup}, { startup.impact_value}\n')
                continue
            lan_inv = set(investor.languages)
            lan_stp = set(startup.team_languages)
            common_languages = lan_inv.intersection(lan_stp)
            # filtro capital
            if not startup.capital >= investor.capital[0] or not startup.capital<=investor.capital[1]:
                print(f'(3) - capital filter not passed:\n. Investor: {investor}, {investor.capital} \n. Startup: {startup} {startup.capital}\n')
                continue
            # filtro lingue
            if len(common_languages) == 0:
                print(f'(4) - languages filter not passed:\n. Investor: {investor}, {lan_inv}\n. Startup: {startup}, {lan_stp}\n')
                continue
            values_stp = set(startup.team_values)
            values_inv = set(investor.team_values)
            common_values = values_stp.intersection(values_inv)
            stage_stp = startup.stage
            stage_inv = investor.stage
            #filtro stage
            if stage_stp not in stage_inv:
                print(f'(5) - stage filter not passed:\n. Investor: {investor}, {stage_inv} \n. Startup: {startup}, {stage_stp}\n')
                continue
            # filtro team_values
            if len(common_values) == 0:
                print(f'(6) - common values filter not passed:\n. Investor: {investor}, {values_inv}\n. Startup: {startup}, {values_stp}\n')
                continue
            else:
                score = 50
                if len(common_values) >= 3:
                    score += 10
                if startup.financial_tables:
                    score += 5
                motives_stp = set(startup.team_motives)
                motive_inv = set(investor.team_motives)
                common_motives = motives_stp.intersection(motive_inv)
                if len(common_motives) > 0:
                    score += 10
                expertice_stp = set(startup.investor_expertise)
                expertice_inv = set(investor.investor_expertise)
                common_expertice = expertice_stp.intersection(expertice_inv)
                if len(common_expertice) > 0:
                    score += 5
                    if len(common_expertice)>3:
                        score +=5
                founds_use_stp = set(startup.use_of_funds.keys())
                use_founds_intersect=expertice_inv.intersection(founds_use_stp)
                if len(use_founds_intersect) > 0:
                    score += 5
                matches.append((startup, investor, score))

matching()
matches

                    