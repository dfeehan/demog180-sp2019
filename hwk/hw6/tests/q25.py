test = {
  'name': 'q25',
  'points': 5,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> sim_results.num_rows
          800
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.round(np.mean(sim_results['num_infected_random']), 0)
          71.0
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
