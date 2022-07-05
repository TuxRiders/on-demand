from paraview import python_view

def setup_data(view):
    pass

def render(view, width, height):
    figure = python_view.matplotlib_figure(width, height)

    ax = figure.add_subplot(1,1,1)
    ax.minorticks_on()
    ax.set_title('Plot title')
    ax.set_xlabel('X label')
    ax.set_ylabel('Y label')

    # Process only the first visible object in the pipeline browser
    dataObject = view.GetVisibleDataObjectForRendering(0)

    x = dataObject.GetPointData().GetArray('RTData')

    # Convert VTK data array to numpy array for plotting
    from paraview.numpy_support import vtk_to_numpy
    np_x = vtk_to_numpy(x)

    ax.hist(np_x, bins=20)

    return python_view.figure_to_image(figure)
