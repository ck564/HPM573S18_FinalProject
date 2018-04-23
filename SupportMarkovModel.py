import InputData as Data
import scr.FormatFunctions as Format

def print_outcomes(simOutput, treatment):

    # mean and CI text for patient survival time
    survival_mean_CI_text = Format.format_estimate_interval(
        estimate=simOutput.get_sumStat_survival_times().get_mean(),
        interval=simOutput.get_sumStat_survival_times().get_t_CI(alpha=Data.ALPHA),
        deci=2
    )

    # mean and CI text of discounted total cost
    cost_mean_CI_text = Format.format_estimate_interval(
        estimate=simOutput.get_sumStat_costs().get_mean(),
        interval=simOutput.get_sumStat_costs().get_t_CI(alpha=Data.ALPHA),
        deci=2
    )

    # mean and CI text of discounted utility
    utility_mean_CI_text = Format.format_estimate_interval(
        estimate=simOutput.get_sumStat_utilities().get_mean(),
        interval=simOutput.get_sumStat_utilities().get_t_CI(alpha=Data.ALPHA),
        deci=2
    )

    # print outcomes
    print(treatment)
    print(" Estimate of mean survival time and {:.{prec}%} confidence interval:".format(1 - Data.ALPHA, prec=0),
          survival_mean_CI_text)
    print(" Estimate of discounted cost and {:.{prec}%} confidence interval:".format(1 - Data.ALPHA, prec=0),
          cost_mean_CI_text)
    print(" Estimate of discounted utility and {:.{prec}%} confidence interval:".format(1 - Data.ALPHA, prec=0),
          utility_mean_CI_text)
