from paraview import python_view
import numpy  as np

def setup_data(view):
    # for i in xrange(view.GetNumberOfVisibleDataObjects()):
    #     dataObject = view.GetVisibleDataObjectForSetup(i)
    #     view.SetAttributeArrayStatus(i, vtkDataObject.POINT, "XXX", 1)
    view.EnableAllAttributeArrays()

def render(view, width, height):
    figure = python_view.matplotlib_figure(width, height)

    ax1 = figure.add_subplot(2,1,1)
    ax1.minorticks_on()
    ax1.set_title('Plot title')
    ax1.set_xlabel('X label')
    ax1.set_ylabel('Y label')

    # Process only the first visible object in the pipeline browser
    dataObject = view.GetVisibleDataObjectForRendering(0)

    x = dataObject.GetPointData().GetArray('RTData')

    # Convert VTK data array to numpy array for plotting
    from paraview.numpy_support import vtk_to_numpy
    np_x = vtk_to_numpy(x)

    ax1.hist(np_x, bins=20)

    ax2 = figure.add_subplot(2,1,2)
    ax2.minorticks_on()
    ax2.set_title('Plot title 2')
    ax2.set_xlabel('X label')
    ax2.set_ylabel('Y label')

    dataObject_line = view.GetVisibleDataObjectForRendering(1)

    x_line = dataObject_line.GetPointData().GetArray('arc_length')
    y_line = dataObject_line.GetPointData().GetArray('RTData')

    np_x_line = vtk_to_numpy(x_line)
    np_y_line = vtk_to_numpy(y_line)

    ax2.plot(np_x_line, np_y_line, "o")

    x_interp = np.linspace(np.min(np_x_line), np.max(np_x_line), 100)
    y_interp = np.interp(x_interp, np_x_line, np_y_line)

    ax2.plot(x_interp, y_interp, "r--")

    return python_view.figure_to_image(figure)
